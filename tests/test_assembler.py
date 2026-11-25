import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from assembler import assemble

class AssemblerChecks(unittest.TestCase):
    def test_a_and_c_instructions(self):
        code, errors, _=assemble(["@2","D=A","@3","D=D+A","@0","M=D"])
        self.assertEqual(errors,[])
        self.assertEqual(len(code),6)
        self.assertTrue(all(len(x)==16 for x in code))
    def test_labels_and_variables(self):
        code, errors, symbols=assemble(["@total","M=1","(AGAIN)","@AGAIN","0;JMP"])
        self.assertEqual(errors,[])
        self.assertEqual(symbols["total"],16)
        self.assertEqual(symbols["AGAIN"],2)
        self.assertEqual(code[2],"0000000000000010")
    def test_predefined_symbols(self):
        code, errors, _=assemble(["@SCREEN","@KBD","@R7"])
        self.assertEqual(errors,[])
        self.assertEqual(code,["0100000000000000","0110000000000000","0000000000000111"])
    def test_invalid_mnemonic_reported(self):
        _, errors, _=assemble(["D=Q+1"])
        self.assertEqual(len(errors),1)
        self.assertIn("Line 1",errors[0])
    def test_range_validation(self):
        _, errors, _=assemble(["@40000"])
        self.assertTrue(errors)

if __name__=="__main__": unittest.main(verbosity=2)
