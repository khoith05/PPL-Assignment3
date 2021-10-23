import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    ####################
    #    Redeclared    #
    ####################

    def test_0(self):
        input="""
        class Add{
            int a;
            float a;
        }
          """
        
        expect="Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,400))

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
                    final string b=\"12\",a=\"ab\";
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

        ##################
        #   Undeclared   # 
        ##################

    def test_16(self):#fix
        input="""
        class Add{
            int main(){
                int a=b+1;
            }
        }
        """
        expect="Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_17(self):#problem
        input="""
        class Add{
            float[4] a;
            int main(){
                b:=this.a[3];
            }
        }
        """
        expect="Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_18(self):
        input="""
        class Add{
            int main(int b){
                for a:=1 to 10 do{
                    b:=b+9;
                }
            }
        }
        """
        expect="Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_19(self):#problem
        input="""
        class Add{
            int main(){
                return a+100;
            }
        }
        """
        expect="Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_20(self):#problem
        input="""
        class Add {
            int main(float b){
                if a==1 then
                    return b;
            }
        }
        """
        expect="Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_21(self):
        input="""
        class Add {
            int main(){
                {
                    int a=b+3;
                }
            }
        }
        """
        expect="Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_22(self):
        input="""
        class Add {
            int main(int b){
                if 3>1 then 
                {
                    int a=b+3;
                    {
                        a:=b-c;
                    }
                }
            }
        }
        """
        expect="Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_23(self):
        input="""
        class Add {
            int main(int a,b){
               for a:=b+c to 10 do{
                    b:=b+b;
               }          
            }
        }
        """
        expect="Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_24(self):
        input="""
        class Shape {
            float a;
            static float b;
            final float c=5.5;
            Add d=new Add();
            Sub e=new Sub();
            void foo(){
            }
            static float getb(){
                Shape.b:=Shape.b+this.a;
                return Shape.b;
            }
            
        }
        class Sub extends Shape{
            Shape a= new Shape();
            void func(){
                this.a.foo();

            }
        }
        class Add extends Sub{
            int main(){
                Shape A;
                this.a.foo();
                this.c:=this.a.a+Shape.b;
                A:=new Add();
                A:=this.a.foo();

                
            }
            
        }
        """
        expect="Type Mismatch In Expression: CallExpr(FieldAccess(Self(),Id(a)),Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_25(self):
        input="""
        class Add {
            int main(int a,b){
                for a:=b to c+b do{
                    b:=b+1;
                }
                
            }
        }
        """
        expect="Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_26(self):
        input="""
        class Add {
            int main(int a,b,c){
                for a:=b to c+b do{
                    b:=b+1;
                    {
                        if d==c then {
                            b:=b+2;
                        }
                    }
                }
                
            }
        }
        """
        expect="Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_27(self):
        input="""
        class Shape{
            static int foo(int a){
                return a+1;
            }
        }
        class Add {
            int main(int a,b,c){
                a:=Shape.foo(d);
                
            }
        }
        """
        expect="Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_28(self):
        input="""
        class Add {
            int main(int[4] a){
                a[c]:=10;
            }
        }
        """
        expect="Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_29(self):#problem 
        input="""
        class Add{
            int a=this.b+1;
        }

        """
        expect="Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_30(self):
        input="""
        class Add{
            int main(){
                int a= this.b;
            }
        }
        """
        expect="Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_31(self):
        input="""
        class Shape{
            int s=7;
            Shape(int a){
                this.s:=a;
            }
        }
        class Add{
            Shape a=new Shape(this.b);
            int main(){
                int a= this.a.s;
            }
        }
        """
        expect="Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_32(self):
        input="""
        class Shape{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
        }
        class Add extends Shape{
            Shape a=new Shape(this.s);
            int main(){
                Shape b=new Shape(c);
            }
        }
        """
        expect="Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_33(self):
        input="""
        class Shape{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Add extends Shape{
            Shape a=new Shape(this.s);
            Shape b=this.a.foo(this.c);
            int main(int c){
                Shape b=new Shape(c);
            }
        }
        """
        expect="Undeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_34(self):#problem
        input="""
        class Shape{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Add extends Shape{
            int c=7;
            Shape a=new Shape(this.s);
            Shape b=this.a.foo(this.c);
            int main(int c){
                this.s:=3;
                this.d:=4;
            }
        }
        """
        expect="Undeclared Attribute: d"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_35(self):#problem
        input="""
        class Shape{
            int s=1;
            int c=7;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Add extends Shape{
            Shape a=new Shape(this.s);
            Shape b=this.a.foo(this.c);
            int d=7;
            int main(int c){
                this.s:=3;
                this.d:=4;
                Shape.f:=6;
            }
        }
        """
        expect="Undeclared Attribute: f"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_36(self):#problem-fixed
        input="""
        class Shape{
            int s=1;
            int c=9;
            static int f;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Add extends Shape{
            Shape a=new Shape(this.s);
            Shape b=this.a.foo(this.c);
            int d=7;
            int main(int c){
                this.s:=3;
                this.d:=4;
                Shape.f:=6;
                c:=Shape.r+7;
            }
        }
        """
        expect="Undeclared Attribute: r"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_37(self):
        input="""
        class Shape{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Sub extends Shape{
            static float a=7.6;
        }
        class Add extends Sub{
            float a=this.a+this.s;
            int[4] d;
            int main(int c){
                this.d[this.f]:=c;
            }
        }

        """
        expect="Undeclared Attribute: f"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_38(self):#problem
        input="""
        class Shape{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Sub extends Shape{
            static float a=7.6;
        }
        class Add extends Sub{
            float a=this.a+this.s;
            Sub d=new Sub(7);
            int main(int c){
                this.d.s:=7;
                this.d.e:=6;
            }
        }
        """ 
        expect="Undeclared Attribute: e"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_39(self):#problem
        input="""
        class Shape{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Sub extends Shape{
            static float a=7.6;
        }
        class Add extends Sub{
            float a=this.a+this.s;
            int main(int c){
                return this.c;
            }
        }
        """
        expect="Undeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_40(self):#problem
        input="""
        class Shape{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Sub extends Shape{
            static float a=7.6;
        }
        class Add extends Sub{
            float a=this.a+this.s;
            Shape d=new Shape(7);
            int main(Shape c){
                c:=this.d.foo(6);
                this.d.fuu();
            }
        }
        """
        expect="Undeclared Method: fuu"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self):#problem
        input="""
        class Shape{
            int s=1;
            Shape foo(int a){
                return new Shape();
            }
        }
        class Sub extends Shape{
            static float a=7.6;
        }
        class Add extends Sub{
            float a=this.a+this.s;
            Sub d=new Sub();
            int main(Shape c){
                c:=this.d.foo(7);
                Shape.fuu();
            }
        }
        """
        expect="Undeclared Method: fuu"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_42(self):#problem
        input="""
        class Shape{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Sub extends Shape{
            static float a=7.6;
            Sub(int a){
                Sub.a:=a;
            }
        }
        class Add extends Sub{
            Sub d=new Sub(7);
            int main(int c){
                Flash f=new Flash();
            }
        }
        """
        expect="Undeclared Class: Flash"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_43(self):
        input="""
        class Shape{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Sub extends Shape{
            static float a=7.6;
        }
        class Add extends Sub{
            Sub d=new Sub(7);
            Flash f=new Flash();
            int main(int c){
                return c;
            }
        }
        """
        expect="Undeclared Class: Flash"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_44(self):#problem find innit from parent
        input="""
        class Shape{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Sub extends Shape{
            static float a=7.6;
            Sub(int a){
                Sub.a:=a;
            }
        }
        class Add extends Sub{
            Sub d=new Sub(7);
            Mul main(int c){
                return c;
            }
        }
        """
        expect="Undeclared Class: Mul"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_45(self):
        input="""
        class Shape extends Mul{
            int s=1;
            Shape(int a){
                this.s:=a;
            }
            Shape foo(int a){
                return new Shape(a);
            }
        }
        class Sub extends Shape{
            static float a=7.6;
        }
        class Add extends Sub{
            Sub d=new Sub(7);
            int main(int c){
                return c;
            }
        }"""
        expect="Undeclared Class: Mul"
        self.assertTrue(TestChecker.test(input,expect,445))

    ######################################
    #     Type mismatch in Expression    #
    ######################################

    def test_46(self):
        input="""
        class Add{
            int main(){
                int a;
                a[1]:=3;
            }
        }
        
        """
        expect="Type Mismatch In Expression: ArrayCell(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_47(self):
        input="""
        class Add{
            void main(){
                int[4] a;
                a[1.2]:=3;
            }
        }
        """
        expect="Type Mismatch In Expression: ArrayCell(Id(a),FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_48(self):
        input="""
        class Add{
            void main(){
                int[4] a;
                float b=2.0;
                a[b]:=3;
            }
        }
        """
        expect="Type Mismatch In Expression: ArrayCell(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_49(self):
        input="""
        class Add{
            void main(){
                int[4] a;
                float b=2.0;
                a[\"2\"]:=3;
            }
        }
        """
        expect="Type Mismatch In Expression: ArrayCell(Id(a),StringLit(\"2\"))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_50(self):
        input="""
        class Add{
            void main(){
                Add a;
                a[2]:=3;
            }
        }
        """
        expect="Type Mismatch In Expression: ArrayCell(Id(a),IntLit(2))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_51(self):
        input="""
        class Add{
            void main(){
                int a=1+1;
                boolean b;
                float c;
                a:=2*3;
                a:=4-3;
                b:=a>c;
                b:=a<c;
                b:=a<=c;
                b:=a>=c;
                b:=a==3;
                b:=a!=4;
                a:=5\\6;
                a:=7%3;
                a:=-a;
                a:=+a;
                a:=4/5;

            }
        }
        """
        expect="Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,IntLit(4),IntLit(5)))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_52(self):
        input="""
        class Add{
            void main(){
                int a;
                boolean b;
                float c;
                c:=1.1+3.3;
                c:=4.4-5;
                c:=1.3*2.3;
                c:=3.3/5.5;
                b:=5.5<5.6;
                b:=5.5>5.6;
                b:=5.5>=5.6;
                b:=5.5<=5.6;
                c:=1+a;
                c:=1.1+a;
                c:=1+1.1;
                c:=a*12.2;
                c:=a/7;
                b:=a>c;
                b:=a<c;
                b:=a<=c;
                b:=a>=c;
                b:=a==b;
            }
        }
        """
        expect="Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_53(self):
        input="""
        class Add{
            void main(){
                boolean a,b,c;
                b:=a==b;
                b:=a!=c;
                b:=a&&c;
                b:=a||c;
                b:=!b;
                b:=b+c;

            }
        }
        """
        expect="Type Mismatch In Statement: AssignStmt(Id(b),BinaryOp(+,Id(b),Id(c)))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_54(self):
        input="""
        class Add{
            int main(){
                string a=\"b\",b=\"c\";
                a:=b^\"sdf\";
                a:=1^b;
            }
        }
        """
        expect="Type Mismatch In Expression: BinaryOp(^,IntLit(1),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_55(self):
        input="""
        class Add{
            int main(){
                int a;
                a.b:=6;
            }
        }
        """
        expect="Type Mismatch In Expression: FieldAccess(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_56(self):
        input="""
        class Add{
            void foo(){}
            int main(){
                Add a;
                a:=this.foo();
            }
        }
        """
        expect="Type Mismatch In Expression: CallExpr(Self(),Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_57(self):
        input="""
        class Shape{
            void foo(){}
        }
        class Add{
            void foo(){}
            int main(){
                Shape a=new Shape();
                int b=a.foo();
            }
        }
        """
        expect="Type Mismatch In Expression: CallExpr(Id(a),Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_58(self):
        input="""
        class Shape{
            Shape(int a; float b){

            }
        }
        class Add extends Shape{
            int main(){
                Add a=new Add(4,5.6);
                Add b=new Add(4,5);
                Add c=new Add(4,5,6);
            }
        }
        """
        expect="Type Mismatch In Expression: NewExpr(Id(Add),[IntLit(4),IntLit(5),IntLit(6)])"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_59(self):
        input="""
        class Shape{
            int foo(int a,b,c){}
            Shape(int a; float b){

            }
        }
        class Add {
            int main(){
                Shape a=new Shape(4,5);
                int d=a.foo(1.1,2,3);
            }
        }"""
        expect="Type Mismatch In Expression: CallExpr(Id(a),Id(foo),[FloatLit(1.1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_60(self):
        input="""
        class Shape{
            static int foo(Add a,b,c){}
            Shape(int a; float b){

            }
        }
        class Add {
            int main(){
                Shape a=new Shape(4,5);
                int c=Shape.foo(new Add(),new Add(),new Add());
                int d=Shape.foo(new Add(),new Add(),c);
            }
        }"""
        expect="Type Mismatch In Expression: CallExpr(Id(Shape),Id(foo),[NewExpr(Id(Add),[]),NewExpr(Id(Add),[]),Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,460))

        ################################
        #  Type mismatch in Statement  #
        ################################
        
    #if
    def test_61(self):
        input="""
        class Add{
            int main(){
                boolean b=true;
                int a;
                if b then
                    a:=1;
                else a:=3;
                if a then {}
            }
        }
        """
        expect="Type Mismatch In Statement: If(Id(a),Block([],[]))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_62(self):
        input="""
        class Add{
            int main(){
                if true then{
                }
                if 1==1 then {}
                if true && true then{}
                if 0 then{}
            }
        }
        """
        expect="Type Mismatch In Statement: If(IntLit(0),Block([],[]))"
        self.assertTrue(TestChecker.test(input,expect,462))
    #for
    def test_63(self):
        input="""
        class Add{
            int main(){
                float b;
                int a;
                for a:=1 to 10 do{}
                for b:=1 to 10 do{}
            }
        }
        """
        expect="Type Mismatch In Statement: For(Id(b),IntLit(1),IntLit(10),True,Block([],[])])"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_64(self):
        input="""
        class Add{
            int main(int c){
                float b;
                int a;
                for a:=c to b do{}
            }
        }
        """
        expect="Type Mismatch In Statement: For(Id(a),Id(c),Id(b),True,Block([],[])])"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_65(self):
        input="""
        class Add{
            int main(int c){
                float b;
                for c:=b to 10+c do{}
            }
        }
        """
        expect="Type Mismatch In Statement: For(Id(c),Id(b),BinaryOp(+,IntLit(10),Id(c)),True,Block([],[])])"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_66(self):
        input="""
        class Add{
            int main(){
                int a;
                a.foo();
            }
        }
        """
        expect="Type Mismatch In Statement: Call(Id(a),Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_67(self):
        input="""
        class Add{
            int a=new Add();
        }
        """
        expect="Type Mismatch In Expression: VarDecl(Id(a),IntType,NewExpr(Id(Add),[]))"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_68(self):
        input="""
        class Add{
            int foo(){}
            int main(){
                this.foo();
            }
        }
        """
        expect="Type Mismatch In Statement: Call(Self(),Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_69(self):
        input="""
        class Add{
            void foo(){}
            int main(){
                this.foo();
                this.foo(3);

            }
        }
        """
        expect="Type Mismatch In Statement: Call(Self(),Id(foo),[IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_70(self):
        input="""
        class Add{
            void foo(int a,b,c;float d,f,g){}
            int main(){
                this.foo(3,4,5,6,7,8);
                this.foo(3);

            }
        }
        """
        expect="Type Mismatch In Statement: Call(Self(),Id(foo),[IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_71(self):
        input="""
        class Add{
            void foo(int a,b,c;float d,f,g){}
            int main(){
                this.foo(3,4,5,6,7,8);
                this.foo(3,4,5,\"dd\",7,8);

            }
        }
        """
        expect="Type Mismatch In Statement: Call(Self(),Id(foo),[IntLit(3),IntLit(4),IntLit(5),StringLit(\"dd\"),IntLit(7),IntLit(8)])"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_72(self):
        input="""
        class Add{
            void foo(string a){}
            int main(){
                this.foo(\"dfdfdf\");
                this.foo(3);

            }
        }"""
        expect="Type Mismatch In Statement: Call(Self(),Id(foo),[IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_73(self):
        input="""
        class Shape{
            static void foo(){
            
            }
            int fuu(){}
            void fii(){}
        }
        class Add{
            int main(){
                Shape.foo();
                new Shape().fii();
                new Shape().fuu();
            }
        }
        """
        expect="Type Mismatch In Statement: Call(NewExpr(Id(Shape),[]),Id(fuu),[])"
        self.assertTrue(TestChecker.test(input,expect,473))
    #return
    def test_74(self):
        input="""
        class Add{
            int main(){
                return 7.5;
            }
        }
        """
        expect="Type Mismatch In Statement: Return(FloatLit(7.5))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_75(self):
        input="""
        class Add{
            int main(){
                int a=5;
                return a;
            }
            float foo(){
                int a;
                return a;
            }
            int fuu(){
                float b;
                return b;
            }
        }
        """
        expect="Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_76(self):
        input="""
        class Shape{
            Shape(int[4] b){}
        }
        class Sub extends Shape{}
        class Add{
            Shape main(){
                Sub a=new Sub({4,5,6,7});
                return a;
            }
            void foo(){
                return 7;
            }
        }
        """
        expect="Type Mismatch In Statement: Return(IntLit(7))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_77(self):
        input="""
        class Shape{}
        class Sub extends Shape{}
        class Add{
            Shape main(){
                {{{{{{Sub a=new Sub();
                return a;}}}}}}
            }
            Sub foo(){
                return new Shape();
            }
        }
        """
        expect="Type Mismatch In Statement: Return(NewExpr(Id(Shape),[]))"
        self.assertTrue(TestChecker.test(input,expect,477))

        #################################
        #   Type mismatch in constant   #
        #################################

    def test_78(self):
        input="""
        class Add{
            int a=8;
            final int b=7.8;
        }
        """
        expect="Type Mismatch In Constant Declaration: ConstDecl(Id(b),IntType,FloatLit(7.8))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_79(self):
        input="""
        class Add{
            int a=8;
            final int[4] b={3,4,5};
        }
        """
        expect="Type Mismatch In Constant Declaration: ConstDecl(Id(b),ArrayType(4,IntType),[IntLit(3),IntLit(4),IntLit(5)])"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_80(self):
        input="""
        class Add{
            int a=8;
            final int[4] b={3,4,5};
        }
        """
        expect="Type Mismatch In Constant Declaration: ConstDecl(Id(b),ArrayType(4,IntType),[IntLit(3),IntLit(4),IntLit(5)])"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_81(self):
        input="""
        class Add{
            int main(){
                final Add a=8;
            }
        }
        """
        expect="Type Mismatch In Constant Declaration: ConstDecl(Id(a),ClassType(Id(Add)),IntLit(8))"
        self.assertTrue(TestChecker.test(input,expect,481))

        ############################
        #   Illegal Array Literal  #
        ############################

    def test_82(self):
        input="""
        class Add{
            float a=8;
            int[4] b={1,2,3,true};
        }
        """
        expect="Illegal Array Literal: [IntLit(1),IntLit(2),IntLit(3),BooleanLit(True)]"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_83(self):
        input="""
        class Add{
            int[4] b={1.1,2,3,4};
        }
        """
        expect="Illegal Array Literal: [FloatLit(1.1),IntLit(2),IntLit(3),IntLit(4)]"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_84(self):
        input="""
        class Add{
            int[4] foo(){}
            int main(){
                float[4] a={1,2,3,4.5};
                #Add[3] b={new Add(),new Add(),new Add()};
                int[4] c=this.foo();
            }
        }
        """
        expect="Illegal Array Literal: [IntLit(1),IntLit(2),IntLit(3),FloatLit(4.5)]"
        self.assertTrue(TestChecker.test(input,expect,484))

    ##############################
    #   Illegal member access    #
    ##############################
    
    def test_85(self):
        input="""
        class Shape{
            int a;
            static int b;
        }
        class Add{
            int a=Shape.a;
        }
        """
        expect=""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_86(self):
        input="""
        class Shape{
            int a;
            static int b;
            int foo(){
            }
            static int fuu(){}
        }
        class Add{
            int a1=Shape.fuu();
            int a3=Shape.b;
            int a2=(new Shape()).a;
            int a=Shape.foo();
        }
        """
        expect="Illegal Member Access: CallExpr(Id(Shape),Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_87(self):
        input="""
        class Shape{
            int a;
            static int b;
            int foo(){
            }
            static int fuu(){}
        }
        class Add{
            Shape a=new Shape();
            int b=a.foo();
            int c=a.fuu();
        }
        """
        expect="Illegal Member Access: CallExpr(Id(a),Id(fuu),[])"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_88(self):
        input="""
        class Shape{
            int a;
            static int b;
            int foo(){
            }
            static int fuu(){}
        }
        class Add{
            Shape a=new Shape();
            int b=a.foo();
            int c=a.b;
        }
        """
        expect="Illegal Member Access: FieldAccess(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,488))

        ##################################
        #   Break/Continue not in Loop   #
        ##################################

    '''def test_89(self):
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
