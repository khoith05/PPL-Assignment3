import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class add{}"""
        expect = str(Program([ClassDecl(Id("add"),[])]))
        print(str(Program([ClassDecl(Id("add"),[])])))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            a:integer;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            a:integer;
            b:integer;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))
   