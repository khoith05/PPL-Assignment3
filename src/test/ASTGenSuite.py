import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
	def test_0(self):
		"""Simple program: class main {} """
		input = """class add{}"""
		expect = str(Program([ClassDecl(Id("add"),[])]))
		self.assertTrue(TestAST.test(input,expect,300))
	def test_1(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{}"""
		expect = str(Program([ClassDecl(Id("add"),[],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,301))
	def test_2(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{
						int[4] a;
					}"""
		expect = str(Program([ClassDecl(Id("add"),[AttributeDecl(Instance(),VarDecl(Id("a"),
			ArrayType(4,IntType())))],Id("Expr"))]))

		self.assertTrue(TestAST.test(input,expect,302))
	def test_3(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{ 
						int[4] a,b,c,_tb;
					}"""
		expect = str(Program([ClassDecl(Id("add"),[AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(4,IntType()))),
		AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(4,IntType()))),
		AttributeDecl(Instance(),VarDecl(Id("c"),ArrayType(4,IntType()))),
		AttributeDecl(Instance(),VarDecl(Id("_tb"),ArrayType(4,IntType())))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,303))
	def test_4(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{ 
						int[4] a,b,c,_tb; 
						float[3] d={1.,3e1,5.2e-2};
					}"""
		expect = str(Program([ClassDecl(Id("add"),[
			AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(4,IntType()))),
			AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(4,IntType()))),
			AttributeDecl(Instance(),VarDecl(Id("c"),ArrayType(4,IntType()))),
			AttributeDecl(Instance(),VarDecl(Id("_tb"),ArrayType(4,IntType()))),
			AttributeDecl(Instance(),VarDecl(Id("d"),ArrayType(3,FloatType()),
				ArrayLiteral([FloatLiteral(1.0),FloatLiteral(30.0),FloatLiteral(0.052)])))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,304))
	def test_5(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{ 
						int[4] a={0012,0340,30,0},b,c={1,2,3,4}; 
						float[3] d={1.,3e1,5.2e-2};
					}"""
		expect = str(Program([ClassDecl(Id("add"),[
			AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(4,IntType()),
				ArrayLiteral([IntLiteral(12),IntLiteral(340),IntLiteral(30),IntLiteral(0)]))),
			AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(4,IntType()))),
			AttributeDecl(Instance(),VarDecl(Id("c"),ArrayType(4,IntType()),
				ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))),
			AttributeDecl(Instance(),VarDecl(Id("d"),ArrayType(3,FloatType()),
				ArrayLiteral([FloatLiteral(1.0),FloatLiteral(30.0),FloatLiteral(0.052)])))]
			,Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,305))
	def test_6(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{ 
						int[4] a={0012,0340,30,0},b,c={1,2,3,4}; 
						float[3] d={1.,3e1,5.2e-2};
						boolean[3] e={true,false,true};
						string[3] f={\"hi\",\"my\",\"name\"};
					}"""
		expect = str(Program([ClassDecl(Id("add"),[
			AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(4,IntType()),
				ArrayLiteral([IntLiteral(12),IntLiteral(340),IntLiteral(30),IntLiteral(0)]))),
			AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(4,IntType()))),
			AttributeDecl(Instance(),VarDecl(Id("c"),ArrayType(4,IntType()),
				ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))),
			AttributeDecl(Instance(),VarDecl(Id("d"),ArrayType(3,FloatType()),
				ArrayLiteral([FloatLiteral(1.0),FloatLiteral(30.0),FloatLiteral(0.052)]))),
			AttributeDecl(Instance(),VarDecl(Id("e"),ArrayType(3,BoolType()),
				ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)]))),
			AttributeDecl(Instance(),VarDecl(Id("f"),ArrayType(3,StringType()),
				ArrayLiteral([StringLiteral("\"hi\""),StringLiteral("\"my\""),StringLiteral("\"name\"")])))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,306))
	def test_7(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{ 
						final int[4] a={0012,0340,30,0},c={1,2,3,4}; 
						static float[3] d={1.,3e1,5.2e-2};
						static final boolean[3] e={true,false,true};
						final static string[3] f={\"hi\",\"my\",\"name\"};
					}"""
		expect = str(Program([ClassDecl(Id("add"),[
			AttributeDecl(Instance(),ConstDecl(Id("a"),ArrayType(4,IntType()),
				ArrayLiteral([IntLiteral(12),IntLiteral(340),IntLiteral(30),IntLiteral(0)]))),
			AttributeDecl(Instance(),ConstDecl(Id("c"),ArrayType(4,IntType()),
				ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))),
			AttributeDecl(Static(),VarDecl(Id("d"),ArrayType(3,FloatType()),
				ArrayLiteral([FloatLiteral(1.0),FloatLiteral(30.0),FloatLiteral(0.052)]))),
			AttributeDecl(Static(),ConstDecl(Id("e"),ArrayType(3,BoolType()),
				ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)]))),
			AttributeDecl(Static(),ConstDecl(Id("f"),ArrayType(3,StringType()),
				ArrayLiteral([StringLiteral("\"hi\""),StringLiteral("\"my\""),StringLiteral("\"name\"")])))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,307))
	def test_8(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{ 
						int a;
					}"""
		expect = str(Program([ClassDecl(Id("add"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,308))
	def test_9(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{ 
						int a,b,c;
					}"""
		expect = str(Program([ClassDecl(Id("add"),[
			AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
			AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),
			AttributeDecl(Instance(),VarDecl(Id("c"),IntType()))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,309))
	def test_10(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{ 
						int a=3,b,c=4;
					}"""
		expect = str(Program([ClassDecl(Id("add"),[
			AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),IntLiteral(3))),
			AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),
			AttributeDecl(Instance(),VarDecl(Id("c"),IntType(),IntLiteral(4)))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,310))
	def test_11(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{ 
						int a=3,b,c=4;
						float d=14e-2;
						boolean e=true;
						string f=\"Hello\";
						Shape s;
					}"""
		expect = str(Program([ClassDecl(Id("add"),[
			AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),IntLiteral(3))),
			AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),
			AttributeDecl(Instance(),VarDecl(Id("c"),IntType(),IntLiteral(4))),
			AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(0.14))),
			AttributeDecl(Instance(),VarDecl(Id("e"),BoolType(),BooleanLiteral(True))),
			AttributeDecl(Instance(),VarDecl(Id("f"),StringType(),StringLiteral("\"Hello\""))),
			AttributeDecl(Instance(),VarDecl(Id("s"),ClassType(Id("Shape"))))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,311))
	def test_12(self):
		"""Simple program: class main {} """
		input = """class add extends Expr{ 
						static int a=3,b,c=4;
						final float d=14e-2;
						static final boolean e=true;
						final static string f=\"Hello\";
						static Shape s;
					}"""
		expect = str(Program([ClassDecl(Id("add"),[
			AttributeDecl(Static(),VarDecl(Id("a"),IntType(),IntLiteral(3))),
			AttributeDecl(Static(),VarDecl(Id("b"),IntType())),
			AttributeDecl(Static(),VarDecl(Id("c"),IntType(),IntLiteral(4))),
			AttributeDecl(Instance(),ConstDecl(Id("d"),FloatType(),FloatLiteral(0.14))),
			AttributeDecl(Static(),ConstDecl(Id("e"),BoolType(),BooleanLiteral(True))),
			AttributeDecl(Static(),ConstDecl(Id("f"),StringType(),StringLiteral("\"Hello\""))),
			AttributeDecl(Static(),VarDecl(Id("s"),ClassType(Id("Shape"))))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,312))

	def test_13(self):
		input = """class add{
						int func(){}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("func"),[],IntType(),Block([],[]))])]))
		self.assertTrue(TestAST.test(input,expect,313))

	def test_14(self):
		input = """class add extends Expr{
						int func(){}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("func"),[],IntType(),Block([],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,314))

	def test_15(self):
		input = """class add extends Expr{
						int func(){}
						float func_1(){}
						boolean func_2(){}
						string func_3(){}
		} """
		expect = str(Program([ClassDecl(Id("add"),[
			MethodDecl(Instance(),Id("func"),[],IntType(),Block([],[])),
			MethodDecl(Instance(),Id("func_1"),[],FloatType(),Block([],[])),
			MethodDecl(Instance(),Id("func_2"),[],BoolType(),Block([],[])),
			MethodDecl(Instance(),Id("func_3"),[],StringType(),Block([],[]))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,315))

	def test_16(self):
		input = """class add extends Expr{
						Shape func(){}
						Shape[4] func_1(){}
		} """
		expect = str(Program([ClassDecl(Id("add"),[
			MethodDecl(Instance(),Id("func"),[],ClassType(Id("Shape")),Block([],[])),
			MethodDecl(Instance(),Id("func_1"),[],ArrayType(4,ClassType(Id("Shape"))),Block([],[]))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,316))

	def test_17(self):
		input = """class add extends Expr{
						static Shape func(){}
						static Shape[4] func_1(){}
		} """
		expect = str(Program([ClassDecl(Id("add"),[
			MethodDecl(Static(),Id("func"),[],ClassType(Id("Shape")),Block([],[])),
			MethodDecl(Static(),Id("func_1"),[],ArrayType(4,ClassType(Id("Shape"))),Block([],[]))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,317))

	def test_18(self):
		input = """class add extends Expr{
						static int func(){}
						static float func_1(){}
						static boolean func_2(){}
						static string func_3(){}
		} """
		expect = str(Program([ClassDecl(Id("add"),[
			MethodDecl(Static(),Id("func"),[],IntType(),Block([],[])),
			MethodDecl(Static(),Id("func_1"),[],FloatType(),Block([],[])),
			MethodDecl(Static(),Id("func_2"),[],BoolType(),Block([],[])),
			MethodDecl(Static(),Id("func_3"),[],StringType(),Block([],[]))],
			Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,318))

	def test_19(self):
		input = """class add {
						int func(int a,b;float c,d;boolean e,f){}
		} """
		expect = str(Program([ClassDecl(Id("add"),[
			MethodDecl(Instance(),Id("func"),[
				VarDecl(Id("a"),IntType()),
				VarDecl(Id("b"),IntType()),
				VarDecl(Id("c"),FloatType()),
				VarDecl(Id("d"),FloatType()),
				VarDecl(Id("e"),BoolType()),
				VarDecl(Id("f"),BoolType())],
			IntType(),Block([],[]))])]))
		self.assertTrue(TestAST.test(input,expect,319))

	def test_20(self):
		input = """class add {
						int func(Shape d){}
		} """
		expect = str(Program([ClassDecl(Id("add"),[
			MethodDecl(Instance(),Id("func"),[VarDecl(Id("d"),ClassType(Id("Shape")))],
			IntType(),Block([],[]))])]))
		self.assertTrue(TestAST.test(input,expect,320))

	def test_21(self):
		input = """class add {
						int func(Shape[4] d;int[4] a; int[2] b){}
		} """
		expect = str(Program([ClassDecl(Id("add"),[
			MethodDecl(Instance(),Id("func"),[
				VarDecl(Id("d"),ArrayType(4,ClassType(Id("Shape")))),
				VarDecl(Id("a"),ArrayType(4,IntType())),
				VarDecl(Id("b"),ArrayType(2,IntType()))],
			IntType(),
			Block([],[]))])]))
		self.assertTrue(TestAST.test(input,expect,321))

	def test_22(self):
		input = """class add{
						float foo(int[3] a, b ,c; float[4] a,d,f){}
		}
		"""
		expect = str(Program([ClassDecl(Id("add"),[
			MethodDecl(Instance(),Id("foo"),[
				VarDecl(Id("a"),ArrayType(3,IntType())),
				VarDecl(Id("b"),ArrayType(3,IntType())),
				VarDecl(Id("c"),ArrayType(3,IntType())),
				VarDecl(Id("a"),ArrayType(4,FloatType())),
				VarDecl(Id("d"),ArrayType(4,FloatType())),
				VarDecl(Id("f"),ArrayType(4,FloatType()))],
			FloatType(),Block([],[]))])]))
		self.assertTrue(TestAST.test(input,expect,322))

	def test_23(self):
		input = """class add{
						int main(){
							int a;
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[
			MethodDecl(Instance(),Id("main"),[],
			IntType(),Block([VarDecl(Id("a"),IntType())],[]))])]))
		self.assertTrue(TestAST.test(input,expect,323))

	def test_24(self):
		input = """class add{
						int main(){
							int a,b,c;
						}
		}  """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[]))])]))
		self.assertTrue(TestAST.test(input,expect,324))

	def test_25(self):
		input = """class add{
						int main(){
							int a=4,b,c=3;
						}
		}  """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(4)),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType(),IntLiteral(3))],[]))])]))
		self.assertTrue(TestAST.test(input,expect,325))

	def test_26(self):
		input = """class add{
						int main(){
							int[3] a={1,2,3},b,c;
						}
		}  """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("b"),ArrayType(3,IntType())),VarDecl(Id("c"),ArrayType(3,IntType()))],[]))])]))
		self.assertTrue(TestAST.test(input,expect,326))

	def test_27(self):
		input = """class add{
						static int main(){
							int[3] a={1,2,3},b,c;
							return a[2];
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Static(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("b"),ArrayType(3,IntType())),VarDecl(Id("c"),ArrayType(3,IntType()))],[Return(ArrayCell(Id("a"),IntLiteral(2)))]))])]))

	def test_28(self):
		input = """class add{
						int main(){
							for i:=1 to 5 do
								break;
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(5),True,Break())]))])]))
		self.assertTrue(TestAST.test(input,expect,328))

	def test_29(self):
		input = """class add{
						int main(){
							for i:=5 downto 1 do
								continue; 
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[For(Id("i"),IntLiteral(5),IntLiteral(1),False,Continue())]))])]))
		self.assertTrue(TestAST.test(input,expect,329))

	def test_30(self):
		input = """class add{
						int main(){
							this.a:=3;
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),IntLiteral(3))]))])]))
		self.assertTrue(TestAST.test(input,expect,330))

	def test_31(self):
		input = """class add{
						int main(){
							int a= 4;
							a:=5;
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(4))],[Assign(Id("a"),IntLiteral(5))]))])]))
		self.assertTrue(TestAST.test(input,expect,331))

	def test_32(self):
		input = """class add{
						int main(){
							if a then
								a:=1;
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[If(Id("a"),Assign(Id("a"),IntLiteral(1)))]))])]))
		self.assertTrue(TestAST.test(input,expect,332))

	def test_33(self):
		input = """class add{
						int main(){
							if a then
								a:=1;
							else
								a:=2;
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[If(Id("a"),Assign(Id("a"),IntLiteral(1)),Assign(Id("a"),IntLiteral(2)))]))])]))
		self.assertTrue(TestAST.test(input,expect,333))

	def test_34(self):
		input = """class add extends Expr{
						int main(int a){
							for i:=12+13-3 to 100 do
								a:=a+1*22;
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[VarDecl(Id("a"),IntType())],IntType(),Block([],[For(Id("i"),BinaryOp("-",BinaryOp("+",IntLiteral(12),IntLiteral(13)),IntLiteral(3)),IntLiteral(100),True,Assign(Id("a"),BinaryOp("+",Id("a"),BinaryOp("*",IntLiteral(1),IntLiteral(22)))))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,334))

	def test_35(self):
		input = """class add extends Expr{
						int main(boolean b,c,d,e,f){
							boolean a = !b||c==d&&e;
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),BoolType()),VarDecl(Id("d"),BoolType()),VarDecl(Id("e"),BoolType()),VarDecl(Id("f"),BoolType())],IntType(),Block([VarDecl(Id("a"),BoolType(),BinaryOp("==",BinaryOp("||",UnaryOp("!",Id("b")),Id("c")),BinaryOp("&&",Id("d"),Id("e"))))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,335))

	def test_36(self):
		input = """class add extends Expr{
						int main(){
							Shape a= new Shape();
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[]))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,336))

	def test_37(self):
		input = """class add extends Expr{
						int main(){
							Shape a= new Shape(b+c,c*d,new Shape());
						}
		}  """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[BinaryOp("+",Id("b"),Id("c")),BinaryOp("*",Id("c"),Id("d")),NewExpr(Id("Shape"),[])]))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,337))

	def test_38(self):
		input = """class add extends Expr{
						int main(){
							Shape a;
							a:= new Shape(b+c,c*d,new Shape());
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ClassType(Id("Shape")))],[Assign(Id("a"),NewExpr(Id("Shape"),[BinaryOp("+",Id("b"),Id("c")),BinaryOp("*",Id("c"),Id("d")),NewExpr(Id("Shape"),[])]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,338))

	def test_39(self):
		input = """class add extends Expr{
						int main(){
							Shape a;
							a:= Shape.length(b+c,c*d,new Shape());
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ClassType(Id("Shape")))],[Assign(Id("a"),CallExpr(Id("Shape"),Id("length"),[BinaryOp("+",Id("b"),Id("c")),BinaryOp("*",Id("c"),Id("d")),NewExpr(Id("Shape"),[])]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,339))

	def test_40(self):
		input = """class add extends Expr{
						int main(){
							for i:=3e7 downto 12 do
							{
								i:=i+20;
							}
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[For(Id("i"),FloatLiteral(30000000.0),IntLiteral(12),False,Block([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(20)))]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,340))

	def test_41(self):
		input = """class add{
					int main(){
						{break;}
						{continue;}
					}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Block([],[Break()]),Block([],[Continue()])]))])]))
		self.assertTrue(TestAST.test(input,expect,341))

	def test_42(self):
		input = """class add extends Expr{
						float main(){
							/*comment

							int a*/
							int a;
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],FloatType(),Block([VarDecl(Id("a"),IntType())],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,342))

	def test_43(self):
		input = """class Add extends Expr{
						Add(int a){
							this.a:=a;
						}
						int foo(int a){}
						float foo(float a){}
						boolean foo(boolean a){
						}
						string foo(string a){

						}

		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a"))])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),FloatType())],FloatType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),BoolType())],BoolType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),StringType())],StringType(),Block([],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,343))

	def test_44(self):
		input = """class Add extends Expr{
						int[4] foo(int a){}
						int[5] foo(int a){}
						float[4] foo(float a){}
						boolean[4] foo(boolean a){
						}
						string[4] foo(string a){

						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],ArrayType(4,IntType()),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],ArrayType(5,IntType()),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),FloatType())],ArrayType(4,FloatType()),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),BoolType())],ArrayType(4,BoolType()),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),StringType())],ArrayType(4,StringType()),Block([],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,344))

	def test_45(self):
		input = """class Add extends Expr{
						static int[4] foo(int a){}
						static int[5] foo(int a){}
						static float[4] foo(float a){}
						static boolean[4] foo(boolean a){
						}
						static string[4] foo(string a){

						}
		}"""
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),IntType())],ArrayType(4,IntType()),Block([],[])),MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),IntType())],ArrayType(5,IntType()),Block([],[])),MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),FloatType())],ArrayType(4,FloatType()),Block([],[])),MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),BoolType())],ArrayType(4,BoolType()),Block([],[])),MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),StringType())],ArrayType(4,StringType()),Block([],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,345))

	def test_46(self):
		input = """class Add extends Expr{
						Add(int a){
							this.a:=a;
						}
						static int foo(int a){}
						static float foo(float a){}
						static boolean foo(boolean a){
						}
						static string foo(string a){

						}

		}  """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a"))])),MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),Block([],[])),MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),FloatType())],FloatType(),Block([],[])),MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),BoolType())],BoolType(),Block([],[])),MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),StringType())],StringType(),Block([],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,346))

	def test_47(self):
		input = """class add extends Expr{ 
						static int a=3,b,c=4;
						final float d=14e-2;
						static final boolean e=true;
						final static string f=\"Hello\";
						static Shape s;
						int[4] foo(int a){}
						int[5] foo(int a){}
						float[4] foo(float a){}
						boolean[4] foo(boolean a){
						}
						string[4] foo(string a){

						}
					}"""
		expect = str(Program([ClassDecl(Id("add"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType(),IntLiteral(3))),AttributeDecl(Static(),VarDecl(Id("b"),IntType())),AttributeDecl(Static(),VarDecl(Id("c"),IntType(),IntLiteral(4))),AttributeDecl(Instance(),ConstDecl(Id("d"),FloatType(),FloatLiteral(0.14))),AttributeDecl(Static(),ConstDecl(Id("e"),BoolType(),BooleanLiteral(True))),AttributeDecl(Static(),ConstDecl(Id("f"),StringType(),StringLiteral("\"Hello\""))),AttributeDecl(Static(),VarDecl(Id("s"),ClassType(Id("Shape")))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],ArrayType(4,IntType()),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],ArrayType(5,IntType()),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),FloatType())],ArrayType(4,FloatType()),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),BoolType())],ArrayType(4,BoolType()),Block([],[])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),StringType())],ArrayType(4,StringType()),Block([],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,347))

	#Expr
	def test_48(self):
		input = """class add extends Expr{
						int main(){
							if a<b then a:=1;
							if a>b then a:=1;
							if a>=b then a:=1;
							if a<=b then a:=1;
						}
		 } """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[If(BinaryOp("<",Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1))),If(BinaryOp(">",Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1))),If(BinaryOp(">=",Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1))),If(BinaryOp("<=",Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1)))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,348))

	def test_49(self):
		input = """class add extends Expr{
						int main(){
							if a==b then a:=1;
							if a!=b then a:=1;
						}
		 }  """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[If(BinaryOp("==",Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1))),If(BinaryOp("!=",Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1)))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,349))

	def test_50(self):
		input = """class add extends Expr{
						int main(){
							if a&&b then a:=1;
							if a||b then a:=1;
						}
		 }  """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[If(BinaryOp("&&",Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1))),If(BinaryOp("||",Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1)))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,350))

	def test_51(self):
		input = """class add extends Expr{
						int main(){
							a:=a+b;
							a:=a-b;
						}
		 }  """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b"))),Assign(Id("a"),BinaryOp("-",Id("a"),Id("b")))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,351))

	def test_52(self):
		input = """class add extends Expr{
						int main(){
							a:=a*b;
							a:=a/b;
							a:=a\\b;
							a:=a%b;
						}
		 }  """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("*",Id("a"),Id("b"))),Assign(Id("a"),BinaryOp("/",Id("a"),Id("b"))),Assign(Id("a"),BinaryOp("\\",Id("a"),Id("b"))),Assign(Id("a"),BinaryOp("%",Id("a"),Id("b")))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,352))

	def test_53(self):
		input = """class add extends Expr{
						int main(){
							a:=a^b;
						}
		 } """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("^",Id("a"),Id("b")))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,353))

	def test_54(self):
		input = """class add extends Expr{
						int main(){
							if !a then b:=1;
						}
		 } """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[If(UnaryOp("!",Id("a")),Assign(Id("b"),IntLiteral(1)))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,354))

	def test_55(self):
		input = """class add extends Expr{
						int main(){
							a:=-a;
							a:=+a;
							a:=+a+a;
						}
		 } """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),UnaryOp("-",Id("a"))),Assign(Id("a"),UnaryOp("+",Id("a"))),Assign(Id("a"),BinaryOp("+",UnaryOp("+",Id("a")),Id("a")))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,355))

	def test_56(self):
		input = """class add extends Expr{
						int main(){
							a:=b[4];
							a:=b[1+a/3];
							a:=b[1+b[3]];
						}
		 } """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(4))),Assign(Id("a"),ArrayCell(Id("b"),BinaryOp("+",IntLiteral(1),BinaryOp("/",Id("a"),IntLiteral(3))))),Assign(Id("a"),ArrayCell(Id("b"),BinaryOp("+",IntLiteral(1),ArrayCell(Id("b"),IntLiteral(3)))))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,356))

	def test_57(self):
		input = """class add extends Expr{
						int main(){
							Shape a=new Shape(2);
							b:=a.length+1;
							c:=a.area();
							c:=a.area(1+1,a+b);
							c:=a.b.c.a;
							c:=a.b.c.area(1\\2,a%b);

						}
		 } """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[IntLiteral(2)]))],[Assign(Id("b"),BinaryOp("+",FieldAccess(Id("a"),Id("length")),IntLiteral(1))),Assign(Id("c"),CallExpr(Id("a"),Id("area"),[])),Assign(Id("c"),CallExpr(Id("a"),Id("area"),[BinaryOp("+",IntLiteral(1),IntLiteral(1)),BinaryOp("+",Id("a"),Id("b"))])),Assign(Id("c"),FieldAccess(FieldAccess(FieldAccess(Id("a"),Id("b")),Id("c")),Id("a"))),Assign(Id("c"),CallExpr(FieldAccess(FieldAccess(Id("a"),Id("b")),Id("c")),Id("area"),[BinaryOp("\\",IntLiteral(1),IntLiteral(2)),BinaryOp("%",Id("a"),Id("b"))]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,357))

	def test_58(self):
		input = """class Add extends Expr{
						int main(){
							Shape a=new Shape();
							Shape a= new Shape(1,1,a%b+c);
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[])),VarDecl(Id("a"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[IntLiteral(1),IntLiteral(1),BinaryOp("+",BinaryOp("%",Id("a"),Id("b")),Id("c"))]))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,358))

	def test_59(self):
		input = """class Add extends Expr{
						int main(){
							a:=b;
							a:=1;
							a:=123e2;
							a:=True;
							a:="333";
							a:=this.c;
							a:=this.a().b().c;
							a:=nil;
						}
		}  """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),Id("b")),Assign(Id("a"),IntLiteral(1)),Assign(Id("a"),FloatLiteral(12300.0)),Assign(Id("a"),Id("True")),Assign(Id("a"),StringLiteral("\"333\"")),Assign(Id("a"),FieldAccess(SelfLiteral(),Id("c"))),Assign(Id("a"),FieldAccess(CallExpr(CallExpr(SelfLiteral(),Id("a"),[]),Id("b"),[]),Id("c"))),Assign(Id("a"),NullLiteral())]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,359))

	def test_60(self):
		input = """class Add extends Expr{
						int main(){
							a:=(b);
							a:=(1)+b;
							a:=(123e2);
							a:=(True)+False;
							a:=(a+b)*c;
							a:=a-(-c);
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),Id("b")),Assign(Id("a"),BinaryOp("+",IntLiteral(1),Id("b"))),Assign(Id("a"),FloatLiteral(12300.0)),Assign(Id("a"),BinaryOp("+",Id("True"),Id("False"))),Assign(Id("a"),BinaryOp("*",BinaryOp("+",Id("a"),Id("b")),Id("c"))),Assign(Id("a"),BinaryOp("-",Id("a"),UnaryOp("-",Id("c"))))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,360))
	#Expr combine
	def test_61(self):
		input = """class Add extends Expr{
						int main(){
							#a:=b>a==a>=b;
							#a:=b>a&&a>=b;
							#a:=b>a*a>=b;
							#a:=b>a+a>=b;
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,361))

	def test_62(self):
		input = """class Add extends Expr{
						int main(){
							#a:=b==a||a!=b;
							#a:=b==a/a!=b;
							#a:=b==a-a!=b;
							#a:=b==a^a!=b;
						}
		}  """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,362))

	def test_63(self):
		input = """class Add extends Expr{
						int main(){
							a:=b&&a+a||b;
							a:=b&&a%a||b;
							a:=b&&(a+a)||b;
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("||",BinaryOp("&&",Id("b"),BinaryOp("+",Id("a"),Id("a"))),Id("b"))),Assign(Id("a"),BinaryOp("||",BinaryOp("&&",Id("b"),BinaryOp("%",Id("a"),Id("a"))),Id("b"))),Assign(Id("a"),BinaryOp("||",BinaryOp("&&",Id("b"),BinaryOp("+",Id("a"),Id("a"))),Id("b")))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,363))

	def test_64(self):
		input = """class Add extends Expr{
						int main(){
							a:=(-a+b*c)*c-e;
							a:=(a)+(b);
							a:=a-b-b-b;
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("-",BinaryOp("*",BinaryOp("+",UnaryOp("-",Id("a")),BinaryOp("*",Id("b"),Id("c"))),Id("c")),Id("e"))),Assign(Id("a"),BinaryOp("+",Id("a"),Id("b"))),Assign(Id("a"),BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("a"),Id("b")),Id("b")),Id("b")))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,364))

	def test_65(self):
		input = """class Add extends Expr{
						int main(){
							
						}
		}  """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,365))

	def test_66(self):
		input = """class Add extends Expr{
						int main(){
							a:=!-a;
							a:=!a[4][5];
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),UnaryOp("!",UnaryOp("-",Id("a")))),Assign(Id("a"),UnaryOp("!",ArrayCell(ArrayCell(Id("a"),IntLiteral(4)),IntLiteral(5))))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,366))

	def test_67(self):
		input = """class Add extends Expr{
						int main(){
							a:=-a-a-a-a;
							a:=+a+a+a+a+(+a)+a;
						}
		}  """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("-",BinaryOp("-",BinaryOp("-",UnaryOp("-",Id("a")),Id("a")),Id("a")),Id("a"))),Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",UnaryOp("+",Id("a")),Id("a")),Id("a")),Id("a")),UnaryOp("+",Id("a"))),Id("a")))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,367))

	def test_68(self):
		input = """class Add extends Expr{
						int main(){
							a:=a[b[2*c[3]]];
							a:=a[2][3][4]+this.a().b()[2][3];
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("b"),BinaryOp("*",IntLiteral(2),ArrayCell(Id("c"),IntLiteral(3)))))),Assign(Id("a"),BinaryOp("+",ArrayCell(ArrayCell(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),ArrayCell(ArrayCell(CallExpr(CallExpr(SelfLiteral(),Id("a"),[]),Id("b"),[]),IntLiteral(2)),IntLiteral(3))))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,368))

	def test_69(self):
		input = """class Add extends Expr{
						int main(){
							a:=a.a.a.a.a;
							a:=a.a.a(a.a.a,a.a.a);
						}
		}  """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),Id("a")),Id("a")),Id("a")),Id("a"))),Assign(Id("a"),CallExpr(FieldAccess(Id("a"),Id("a")),Id("a"),[FieldAccess(FieldAccess(Id("a"),Id("a")),Id("a")),FieldAccess(FieldAccess(Id("a"),Id("a")),Id("a"))]))]))],Id("Expr"))]))

	def test_70(self):
		input = """class Add extends Expr{
						int main(){
							a:=a.a.a.a.a;
							a:=a.a.a(a.a.a,a.a.a);
						}
		}  """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),Id("a")),Id("a")),Id("a")),Id("a"))),Assign(Id("a"),CallExpr(FieldAccess(Id("a"),Id("a")),Id("a"),[FieldAccess(FieldAccess(Id("a"),Id("a")),Id("a")),FieldAccess(FieldAccess(Id("a"),Id("a")),Id("a"))]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,370))

	def test_71(self):
		input = """class Add extends Expr{
						int main(){
							Shape a=new Shape();
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[]))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,371))

	def test_72(self):
		input = """class Add extends Expr{
						int main(){
							Shape a=new Shape();
							a:=new Shape() + a ;
						}
		}  """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[]))],[Assign(Id("a"),BinaryOp("+",NewExpr(Id("Shape"),[]),Id("a")))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,372))
	#stmt
	def test_73(self):
		input = """class Add extends Expr{
						int main(){
							a:=1;
							this.a:=1;
							a[3]:=1;
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),IntLiteral(1)),Assign(FieldAccess(SelfLiteral(),Id("a")),IntLiteral(1)),Assign(ArrayCell(Id("a"),IntLiteral(3)),IntLiteral(1))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,373))

	def test_74(self):
		input = """class Add extends Expr{
						int main(){
							this.a()[3]:=1;
							thia.a().b().a:=1;
						}
		}  """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(ArrayCell(CallExpr(SelfLiteral(),Id("a"),[]),IntLiteral(3)),IntLiteral(1)),Assign(FieldAccess(CallExpr(CallExpr(Id("thia"),Id("a"),[]),Id("b"),[]),Id("a")),IntLiteral(1))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,374))

	def test_75(self):
		input = """class Add extends Expr{
						int main(){
							a.a.a.a:=1;
							a[b[v[2]]]:=1;
						}
		}  """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(FieldAccess(FieldAccess(FieldAccess(Id("a"),Id("a")),Id("a")),Id("a")),IntLiteral(1)),Assign(ArrayCell(Id("a"),ArrayCell(Id("b"),ArrayCell(Id("v"),IntLiteral(2)))),IntLiteral(1))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,375))

	def test_76(self):
		input = """class Add extends Expr{
						int main(){
								{{{{{}}}}}
							}
		}

		"""
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Block([],[Block([],[Block([],[Block([],[Block([],[])])])])])]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,376))

	def test_77(self):
		input = """class Add extends Expr{
						int main(){
								{{{{{}}}}}
							}
		}
		class Add extends Expr{
						int main(){
								{{{{{}}}}}
							}
		}
		class Add extends Expr{
						int main(){
								{{{{{}}}}}
							}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Block([],[Block([],[Block([],[Block([],[Block([],[])])])])])]))],Id("Expr")),ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Block([],[Block([],[Block([],[Block([],[Block([],[])])])])])]))],Id("Expr")),ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Block([],[Block([],[Block([],[Block([],[Block([],[])])])])])]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,377))

	def test_78(self):
		input = """class Add extends Expr{
						int main(){
							for i:=4 downto -1 do {
                    			int v = (a[i]).check();
                    			if v > max then max := v;
                			}
						}
		}"""
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[For(Id("i"),IntLiteral(4),UnaryOp("-",IntLiteral(1)),False,Block([VarDecl(Id("v"),IntType(),CallExpr(ArrayCell(Id("a"),Id("i")),Id("check"),[]))],[If(BinaryOp(">",Id("v"),Id("max")),Assign(Id("max"),Id("v")))]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,378))

	def test_79(self):
		input = """class Add extends Expr{
						int main(){
							if a==1 then
								a:=2;
							else if a>3 then
								a:=4;
							else if a<5 then 
								return a;
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[If(BinaryOp("==",Id("a"),IntLiteral(1)),Assign(Id("a"),IntLiteral(2)),If(BinaryOp(">",Id("a"),IntLiteral(3)),Assign(Id("a"),IntLiteral(4)),If(BinaryOp("<",Id("a"),IntLiteral(5)),Return(Id("a")))))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,379))

	def test_80(self):
		input = """class Add extends Expr{
						int a;
						int b=1;
						int main(){
							for i:=1 to 10 do {
								continue;
							}
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(1))),MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(10),True,Block([],[Continue()]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,380))

	def test_81(self):
		input = """class Add {
						int main(){
							sys.write("Dfdfdfd");
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[CallStmt(Id("sys"),Id("write"),[StringLiteral("\"Dfdfdfd\"")])]))])]))
		self.assertTrue(TestAST.test(input,expect,381))

	def test_82(self):
		input = """class Add{
						int main(){
							if new Expr() ==a then
								break;
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[If(BinaryOp("==",NewExpr(Id("Expr"),[]),Id("a")),Break())]))])]))
		self.assertTrue(TestAST.test(input,expect,382))

	def test_83(self):
		input = """
				class Add extends Expr{
					int main(){
						this.aa(2,3,4).aaa("ddd").a(True,True);
					}
				}
		 """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[CallStmt(CallExpr(CallExpr(SelfLiteral(),Id("aa"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),Id("aaa"),[StringLiteral("\"ddd\"")]),Id("a"),[Id("True"),Id("True")])]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,383))

	def test_84(self):
		input = """class Add extends Expr{
						int main(){
							if a>b then{
								int a;
								a:=1;
							}else a:=2;
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[If(BinaryOp(">",Id("a"),Id("b")),Block([VarDecl(Id("a"),IntType())],[Assign(Id("a"),IntLiteral(1))]),Assign(Id("a"),IntLiteral(2)))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,384))

	def test_85(self):
		input = """class Add extends Expr{
						int main(){
							for i:=5+2 to 5+5+5+5 do{
								if a>b then 
									break;
								else continue;
							}
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[For(Id("i"),BinaryOp("+",IntLiteral(5),IntLiteral(2)),BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(5),IntLiteral(5)),IntLiteral(5)),IntLiteral(5)),True,Block([],[If(BinaryOp(">",Id("a"),Id("b")),Break(),Continue())]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,385))

	def test_86(self):
		input = """class Add extends Expr{
						int main(){
							for i:=5+2 to 5+5+5+5 do{
								if a>b then 
									break;
								else{if a<b then continue; else break;}
							}
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[For(Id("i"),BinaryOp("+",IntLiteral(5),IntLiteral(2)),BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(5),IntLiteral(5)),IntLiteral(5)),IntLiteral(5)),True,Block([],[If(BinaryOp(">",Id("a"),Id("b")),Break(),Block([],[If(BinaryOp("<",Id("a"),Id("b")),Continue(),Break())]))]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,386))

	def test_87(self):
		input = """class Add extends Expr{
						int main(){
							int s = 0;
                			for i := 0 to 5 do
                    			s := s + arr[i];
                			return s;
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("s"),IntType(),IntLiteral(0))],[For(Id("i"),IntLiteral(0),IntLiteral(5),True,Assign(Id("s"),BinaryOp("+",Id("s"),ArrayCell(Id("arr"),Id("i"))))),Return(Id("s"))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,387))

	def test_88(self):
		input = """class Add extends Expr{
						int main(){
							return new Shape();
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Return(NewExpr(Id("Shape"),[]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,388))

	def test_89(self):
		input = """class Add extends Expr{
						int main(){
							for i := 1 to 2 do {
                    			if i > n then continue;
                    			else {
                       				n := i;
                        			if n > f then break;
                    			}
                			}
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(2),True,Block([],[If(BinaryOp(">",Id("i"),Id("n")),Continue(),Block([],[Assign(Id("n"),Id("i")),If(BinaryOp(">",Id("n"),Id("f")),Break())]))]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,389))

	def test_90(self):
		input = """class Add extends Expr{
						int main(){
							Shape s= new Shape();	
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("s"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[]))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,390))

	def test_91(self):
		input = """class Add extends Expr{
						int main(){
							Shape[3] s,d,v;
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("s"),ArrayType(3,ClassType(Id("Shape")))),VarDecl(Id("d"),ArrayType(3,ClassType(Id("Shape")))),VarDecl(Id("v"),ArrayType(3,ClassType(Id("Shape"))))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,391))

	def test_92(self):
		input = """class Add extends Expr{
						int main(){
							Shape[4] a={1,2,3,4},b,c,d,c={1,2,3,4};
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ArrayType(4,ClassType(Id("Shape"))),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])),VarDecl(Id("b"),ArrayType(4,ClassType(Id("Shape")))),VarDecl(Id("c"),ArrayType(4,ClassType(Id("Shape")))),VarDecl(Id("d"),ArrayType(4,ClassType(Id("Shape")))),VarDecl(Id("c"),ArrayType(4,ClassType(Id("Shape"))),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,392))

	def test_93(self):
		input = """class Add extends Expr{
						int main(){
							final Shape[4] a={1,2,3,4};
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([ConstDecl(Id("a"),ArrayType(4,ClassType(Id("Shape"))),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,393))

	def test_94(self):
		input = """class Add extends Expr{
						int main(){
							final Shape a = new Shape();
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([ConstDecl(Id("a"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[]))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,394))

	def test_95(self):
		input = """class Add extends Expr{
						int main(){
							final int[4] a={1,2,3};
							final float[4] b={1,1,2};
							final boolean[4] c={true,false,true};
							final string[4] d={"a","b","c"};
							
							
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([ConstDecl(Id("a"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),ConstDecl(Id("b"),ArrayType(4,FloatType()),ArrayLiteral([IntLiteral(1),IntLiteral(1),IntLiteral(2)])),ConstDecl(Id("c"),ArrayType(4,BoolType()),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)])),ConstDecl(Id("d"),ArrayType(4,StringType()),ArrayLiteral([StringLiteral("\"a\""),StringLiteral("\"b\""),StringLiteral("\"c\"")]))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,395))

	def test_96(self):
		input = """class Add extends Expr{
						int main(){
							int[4] a,b,c,d={1,2,3};
							float[4] b;
							boolean[4] c;
							string[4] d={"sds","sdfds","dsf"},v,f;
							
							
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ArrayType(4,IntType())),VarDecl(Id("b"),ArrayType(4,IntType())),VarDecl(Id("c"),ArrayType(4,IntType())),VarDecl(Id("d"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("b"),ArrayType(4,FloatType())),VarDecl(Id("c"),ArrayType(4,BoolType())),VarDecl(Id("d"),ArrayType(4,StringType()),ArrayLiteral([StringLiteral("\"sds\""),StringLiteral("\"sdfds\""),StringLiteral("\"dsf\"")])),VarDecl(Id("v"),ArrayType(4,StringType())),VarDecl(Id("f"),ArrayType(4,StringType()))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,396))

	def test_97(self):
		input = """class Add extends Expr{
						int main(){
							int[4] a;
							float[4] b;
							boolean[4] c;
							string[4] d;
							
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([VarDecl(Id("a"),ArrayType(4,IntType())),VarDecl(Id("b"),ArrayType(4,FloatType())),VarDecl(Id("c"),ArrayType(4,BoolType())),VarDecl(Id("d"),ArrayType(4,StringType()))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,397))

	def test_98(self):
		input = """class Add extends Expr{
						int main(){
							final int a=6;
							final float b=7e2;
							final string c="ddfdf";
							final boolean d=true;
						}
		} """
		expect = str(Program([ClassDecl(Id("Add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([ConstDecl(Id("a"),IntType(),IntLiteral(6)),ConstDecl(Id("b"),FloatType(),FloatLiteral(700.0)),ConstDecl(Id("c"),StringType(),StringLiteral("\"ddfdf\"")),ConstDecl(Id("d"),BoolType(),BooleanLiteral(True))],[]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,398))

	def test_99(self):
		input = """class add extends Expr{
						int main(){
							if a<a then {} else {}
						}
		} """
		expect = str(Program([ClassDecl(Id("add"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[If(BinaryOp("<",Id("a"),Id("a")),Block([],[]),Block([],[]))]))],Id("Expr"))]))
		self.assertTrue(TestAST.test(input,expect,399))


