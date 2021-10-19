import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_(self):
    #     input="""
    #       """
    #     expect=""
    #     self.assertTrue(TestChecker.test(input,expect,0))

    def test_1(self):
        input="""
            class Add{
                int a;
                int a;
            }

        """
        expect="Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_2(self):
        input="""
            class Add{
                int a;
            }
            class Add{
                int b;
            }

        """
        expect="Redeclared Class: Add"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_3(self):
        input="""
            class Add{
                int foo(){}
                float foo(){}
            }
        """
        expect="Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_4(self):
        input="""
            class Add{
                int foo;
                float foo(){}
            }
        """
        expect="Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_5(self):
        input="""
            class Add{
                int foo(){
                    int a,a;
                }
            }
        """
        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_6(self):
        input="""
            class Add{
                float foo(int a){
                    int a=6;
                }
            }
        """
        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_7(self):
        input="""
            class Add{
                int main(int a; float b;string a){
                    return a;
                }
            }
        """
        expect="Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_8(self):
        input="""
            class Add{
                int main(){
                    int a=7;
                    {
                        int a=2;
                        int b=1;
                        float b;
                    }
                }
            }
        """
        expect="Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_9(self):
        input="""
            class Add{
                int a;
                final int a=7;
            }
        """
        expect="Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_10(self):
        input="""
            class Add{
                int main(){
                    int a;
                    final float a=5.2;
                }
            }
        """
        expect="Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_11(self):
        input="""
            class Shape{}
            class Add{
                int main(){
                    final int a=1;
                    final string b="12",a="ab";
                }
            }
        """
        expect="Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_12(self):
        input="""
            class Add{
                int main(int a){
                    if a==1 then {
                        int a=3;
                        int b,b;
                    }
                }
            }
        """
        expect="Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_13(self):
        input="""
            class Add{
                int main(int a){
                    int i;
                    for i:=1 to 10 do {
                        int i;
                        int a;
                        int b,b;
                    }
                }
            }
        """
        expect="Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_14(self):
        input="""
            class Add{
                int main(int a){
                    if a==1 then 
                        a:=a+1;
                    else if a==2 then {
                        int a;
                        int c;
                        final float c=5.4;
                    }
                }
            }
        """
        expect="Redeclared Constant: c"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_15(self):
        input="""
            class Add{
                int main(int a){
                    for a:=1 to 10 do 
                        if a==3 then {
                            int a;
                            final int c=1,c=2;
                        }
                }
            }
        """
        expect="Redeclared Constant: c"
        self.assertTrue(TestChecker.test(input,expect,415))

    '''def test_16(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_17(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_18(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_19(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_20(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_21(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_22(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_23(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_24(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_25(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_26(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_27(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_28(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_29(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_30(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_31(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_32(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_33(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_34(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_35(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_36(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_37(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_38(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_39(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_40(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_42(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_43(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_44(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_45(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_46(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_47(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_48(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_49(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_50(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_51(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_52(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_53(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_54(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_55(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_56(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_57(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_58(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_59(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_60(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_61(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_62(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_63(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_64(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_65(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_66(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_67(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_68(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_69(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_70(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_71(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_72(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_73(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_74(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_75(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_76(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_77(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_78(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_79(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_80(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_81(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_82(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_83(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_84(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_85(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_86(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_87(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_88(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_89(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_90(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_91(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_92(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_93(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_94(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_95(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_96(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_97(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_98(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_99(self):
        input=""""""
        expect=""
        self.assertTrue(TestChecker.test(input,expect,499))'''



    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {foo();}"""
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn();
    #     }"""
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,405))
