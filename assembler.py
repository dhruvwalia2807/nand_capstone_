"""Two-pass assembler for the Hack machine language (Nand2Tetris)."""
import re
import sys
from pathlib import Path

COMP = {
"0":"0101010","1":"0111111","-1":"0111010","D":"0001100","A":"0110000",
"!D":"0001101","!A":"0110001","-D":"0001111","-A":"0110011","D+1":"0011111",
"A+1":"0110111","D-1":"0001110","A-1":"0110010","D+A":"0000010","D-A":"0010011",
"A-D":"0000111","D&A":"0000000","D|A":"0010101","M":"1110000","!M":"1110001",
"-M":"1110011","M+1":"1110111","M-1":"1110010","D+M":"1000010","D-M":"1010011",
"M-D":"1000111","D&M":"1000000","D|M":"1010101"}
DEST={"":"000","M":"001","D":"010","MD":"011","A":"100","AM":"101","AD":"110","AMD":"111"}
JUMP={"":"000","JGT":"001","JEQ":"010","JGE":"011","JLT":"100","JNE":"101","JLE":"110","JMP":"111"}
PREDEFINED={"SP":0,"LCL":1,"ARG":2,"THIS":3,"THAT":4,"SCREEN":16384,"KBD":24576}
PREDEFINED.update({f"R{i}":i for i in range(16)})
SYMBOL=re.compile(r"^[A-Za-z_.$:][A-Za-z0-9_.$:]*$")

def normalize(line):
    return re.sub(r"\s+","",line.split("//",1)[0])

def first_pass(source):
    table=dict(PREDEFINED)
    commands=[]
    errors=[]
    for line_no, raw in enumerate(source,1):
        item=normalize(raw)
        if not item: continue
        if item.startswith("("):
            label=item[1:-1] if item.endswith(")") else ""
            if not SYMBOL.fullmatch(label):
                errors.append(f"Line {line_no}: malformed label")
            elif label in table:
                errors.append(f"Line {line_no}: duplicate symbol {label}")
            else:
                table[label]=len(commands)
        else:
            commands.append((line_no,item))
    return table,commands,errors

def assemble(source):
    symbols, commands, errors=first_pass(source)
    result=[]
    next_variable=16
    for line_no, cmd in commands:
        try:
            if cmd.startswith("@"):
                key=cmd[1:]
                if key.isdigit():
                    number=int(key)
                elif SYMBOL.fullmatch(key):
                    if key not in symbols:
                        symbols[key]=next_variable
                        next_variable+=1
                    number=symbols[key]
                else:
                    raise ValueError("invalid A-instruction")
                if not 0 <= number <= 32767:
                    raise ValueError("A-instruction value must be 0..32767")
                word=f"{number:016b}"
            else:
                if cmd.count("=")>1 or cmd.count(";")>1:
                    raise ValueError("malformed C-instruction")
                left, sep, right=cmd.partition("=")
                dest=left if sep else ""
                body=right if sep else cmd
                comp, semi, jump=body.partition(";")
                if comp not in COMP or dest not in DEST or jump not in JUMP:
                    raise ValueError("unknown comp, dest, or jump mnemonic")
                word="111"+COMP[comp]+DEST[dest]+JUMP[jump]
            result.append(word)
        except ValueError as exc:
            errors.append(f"Line {line_no}: {exc}")
    return result, errors, symbols

def main():
    if len(sys.argv) not in (2,3):
        print("Usage: python assembler.py input.asm [output.hack]")
        return 2
    src=Path(sys.argv[1])
    dst=Path(sys.argv[2]) if len(sys.argv)==3 else src.with_suffix(".hack")
    try:
        code, errors, _=assemble(src.read_text(encoding="utf-8").splitlines())
    except OSError as exc:
        print(f"File error: {exc}")
        return 2
    if errors:
        print("\n".join(errors))
        print(f"Assembly stopped: {len(errors)} error(s).")
        return 1
    dst.write_text("\n".join(code)+"\n",encoding="utf-8")
    print(f"Assembly successful: {len(code)} instruction(s).")
    print(f"Machine code saved to: {dst}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
