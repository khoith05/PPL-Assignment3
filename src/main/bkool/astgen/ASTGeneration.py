from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):


    # program: class_decl_lst EOF;
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return Program(ctx.class_decl_lst().accept(self))


    # class_decl_lst: class_decl class_decl_lst| class_decl;
    def visitClass_decl_lst(self, ctx:BKOOLParser.Class_decl_lstContext):
        if ctx.getChildCount()==1:
            return [ctx.class_decl().accept(self)]            
        else:
            return [ctx.class_decl().accept(self)]+ ctx.class_decl_lst().accept(self)
            


    # class_decl: CLASS_LIT ID (EXTEND_LIT ID)? LCB decl_lst RCB ;
    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
        if ctx.ID(1)== None:
            return ClassDecl(Id(ctx.ID(0).getText()),ctx.decl_lst().accept(self))
        else:
            return ClassDecl(Id(ctx.ID(0).getText()),ctx.decl_lst().accept(self),Id(ctx.ID(1).getText()))


    # decl_lst: vm_decl decl_lst | ;
    def visitDecl_lst(self, ctx:BKOOLParser.Decl_lstContext):
        if ctx.getChildCount()==0:
            return []
        else:
            return ctx.vm_decl().accept(self)+ ctx.decl_lst().accept(self)


    # vm_decl : var_decl | method_decl |array_decl; 
    def visitVm_decl(self, ctx:BKOOLParser.Vm_declContext):
        if ctx.var_decl()!=None:
            return ctx.var_decl().accept(self)
        elif ctx.method_decl() !=None:
            return ctx.method_decl().accept(self)
        else:
            return ctx.array_decl().accept(self)


    # array_decl: var_decl_pre array_type array_lst SEMI;
    def visitArray_decl(self, ctx:BKOOLParser.Array_declContext):
        declPre=ctx.var_decl_pre().accept(self)  #(Instance| Static), (Final)?
        varPre=declPre[0]                        #Instance or Static
        arrayList=ctx.array_lst().accept(self)   # ID, Init_Value
        reval=[]                                 #return value
        if len(declPre)==2:
            for i in range(len(arrayList)):
                reval=reval+[AttributeDecl(varPre,ConstDecl(arrayList[i][0],ctx.array_type().accept(self),arrayList[i][1]))]
        else:
            for i in range(len(arrayList)):
                if len(arrayList[i])==2:
                    reval=reval=reval+[AttributeDecl(varPre,VarDecl(arrayList[i][0],ctx.array_type().accept(self),arrayList[i][1]))]
                else:
                    reval=reval+[AttributeDecl(varPre,VarDecl(arrayList[i][0],ctx.array_type().accept(self)))]
        return reval

    # array_type:vdecl_type LSB INTMT RSB;
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return ArrayType(ctx.INTMT().getText(),ctx.vdecl_type().accept(self))


    # array_lst: array_assign COMMA array_lst| array_assign;
    def visitArray_lst(self, ctx:BKOOLParser.Array_lstContext):
        if ctx.getChildCount()==1:
            return [ctx.array_assign().accept(self)]
        else:
            return [ctx.array_assign().accept(self)]+ ctx.array_lst().accept(self)


    # array_assign: ID '=' LCB array_value RCB|ID | ID '=' expr;
    def visitArray_assign(self, ctx:BKOOLParser.Array_assignContext):
        if ctx.getChildCount()==1:
            return [Id(ctx.ID().getText())]
        elif ctx.getChildCount()==3:
            return [Id(ctx.ID().getText()),ctx.expr().getText()]
        else:
            return [Id(ctx.ID().getText()),ArrayLiteral(ctx.array_value().accept(self))]


    # array_value: array_val COMMA array_value|array_val;
    def visitArray_value(self, ctx:BKOOLParser.Array_valueContext):
        if ctx.getChildCount()==1:
            return [ctx.array_val().accept(self)]
        else:
            return [ctx.array_val().accept(self)]+ctx.array_value().accept(self)


    # array_val: BOOLMT|STRINGMT|INTMT|FLOATMT;
    def visitArray_val(self, ctx:BKOOLParser.Array_valContext):
        if ctx.BOOLMT() != None:
            return BooleanLiteral(True if ctx.BOOLMT().getText()=="true" else False)
        elif ctx.STRINGMT() != None:
            return StringLiteral(ctx.STRINGMT().getText())
        elif ctx.INTMT() != None:
            return IntLiteral(int(ctx.INTMT().getText()))
        else:
            return FloatLiteral(float(ctx.FLOATMT().getText()))


    # var_decl:var_decl_pre vdecl_type var_lst SEMI;
    def visitVar_decl(self, ctx:BKOOLParser.Var_declContext):
        declPre=ctx.var_decl_pre().accept(self)  #(Instance| Static), (Final)?
        varPre=declPre[0]                        #Instance or Static
        varList=ctx.var_lst().accept(self)   # ID, Init_Value
        if len(declPre)==2:
            return [AttributeDecl(varPre,ConstDecl(varList[i][0],ctx.vdecl_type().accept(self),varList[i][1])) for i in range(len(varList))]
        else:
            return [AttributeDecl(varPre,VarDecl(varList[i][0],ctx.vdecl_type().accept(self),varList[i][1])) if len(varList[i])==2 else AttributeDecl(varPre,VarDecl(varList[i][0],ctx.vdecl_type().accept(self))) for i in range(len(varList))]


    # var_decl_pre: FINAL_LIT | STATIC_LIT |FINAL_LIT STATIC_LIT |STATIC_LIT FINAL_LIT | ;
    def visitVar_decl_pre(self, ctx:BKOOLParser.Var_decl_preContext):
        reval=[]
        if ctx.STATIC_LIT()!=None:
            reval=reval + [Static()]
        else:
            reval=reval+[Instance()]
        if ctx.FINAL_LIT()!=None:
            reval=reval+["final"]
        return reval


    # vdecl_type: INT_LIT |FLOAT_LIT |BOOL_LIT | STRING_LIT| ID ;
    def visitVdecl_type(self, ctx:BKOOLParser.Vdecl_typeContext):
        if ctx.INT_LIT() != None:
            return IntType()
        elif ctx.FLOAT_LIT() != None:
            return FloatType()
        elif ctx.STRING_LIT() != None:
            return StringType()
        elif ctx.BOOL_LIT() !=None:
            return BoolType()
        else:
            return ClassType(Id(ctx.ID().getText()))


    # var_lst: var_assign COMMA var_lst| var_assign;
    def visitVar_lst(self, ctx:BKOOLParser.Var_lstContext):
        return [ctx.var_assign().accept(self)] if ctx.getChildCount()==1 else [ctx.var_assign().accept(self)]+ ctx.var_lst().accept(self)


    # var_assign: ID '=' expr | ID;
    def visitVar_assign(self, ctx:BKOOLParser.Var_assignContext):
        return [Id(ctx.ID().getText()),ctx.expr().accept(self)] if ctx.getChildCount() == 3 else [Id(ctx.ID().getText())]


    # method_decl:method_decl_pre mdecl_type (ID|MAIN_LIT) LB para_lst? RB block_statement ;
    def visitMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        if str(ctx.mdecl_type().accept(self))=="None":
            return [MethodDecl(Instance(), Id("<init>"),ctx.para_lst().accept(self) if ctx.para_lst()!=None else [],None,ctx.block_statement().accept(self))]
        else:
            return [MethodDecl(ctx.method_decl_pre().accept(self), Id(ctx.getChild(2).getText()),ctx.para_lst().accept(self) if ctx.para_lst()!=None else [],ctx.mdecl_type().accept(self),ctx.block_statement().accept(self))]


    # method_decl_pre: STATIC_LIT | ;
    def visitMethod_decl_pre(self, ctx:BKOOLParser.Method_decl_preContext):
        if ctx.STATIC_LIT()!=None:
            return Static()
        else:
            return Instance()


    #para_lst: para_decl SEMI para_lst | para_decl;
    def visitPara_lst(self, ctx:BKOOLParser.Para_lstContext):
        if ctx.para_lst()!=None:
            return ctx.para_decl().accept(self) +ctx.para_lst().accept(self)
        else:
            return ctx.para_decl().accept(self)
            

    #para_decl:(vdecl_type|array_type) id_lst;
    def visitPara_decl(self, ctx:BKOOLParser.Para_declContext):
        ptype=ctx.vdecl_type().accept(self) if ctx.vdecl_type()!=None else ctx.array_type().accept(self)
        return [VarDecl(x,ptype) for x in ctx.id_lst().accept(self)]


    # id_lst: ID COMMA id_lst |ID;
    def visitId_lst(self, ctx:BKOOLParser.Id_lstContext):
        if ctx.id_lst()!=None:
            return [Id(ctx.ID().getText())]+ctx.id_lst().accept(self)
        else:
            return [Id(ctx.ID().getText())]

    # mdecl_type: vdecl_type| array_type|VOID_LIT|;
    def visitMdecl_type(self, ctx:BKOOLParser.Mdecl_typeContext):
        if ctx.vdecl_type()!=None:
            return ctx.vdecl_type().accept(self)
        elif ctx.array_type()!=None:
            return ctx.array_type().accept(self)
        elif ctx.VOID_LIT()!=None:
            return VoidType()
        else:
            return "None"


    # expr: expr1 (GREAT_OP|LESS_OP|GEQUA_OP|LEQUA_OP) expr1 |expr1;
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        if ctx.getChildCount()==1:
            return ctx.expr1(0).accept(self)
        else:
            return BinaryOp(ctx.getChild(1).getText(),ctx.expr1(0).accept(self),ctx.expr1(1).accept(self))


    # expr1: expr2 (ISEQUA_OP|NEQUA_OP) expr2 | expr2 ;
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        if ctx.getChildCount()==1:
            return ctx.expr2(0).accept(self)
        else:
            return BinaryOp(ctx.getChild(1).getText(),ctx.expr2(0).accept(self),ctx.expr2(1).accept(self))


    # expr2: expr2 (AND_OP| OR_OP) expr3 |expr3;
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        if ctx.getChildCount()==1:
            return ctx.expr3().accept(self)
        else:
            return BinaryOp(ctx.getChild(1).getText(),ctx.expr2().accept(self),ctx.expr3().accept(self))            


    # expr3: expr3 (ADD_OP|SUB_OP) expr4| expr4;
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        if ctx.getChildCount()==1:
            return ctx.expr4().accept(self)
        else:
            return BinaryOp(ctx.getChild(1).getText(),ctx.expr3().accept(self),ctx.expr4().accept(self))


    # expr4: expr4 (MUL_OP|INT_DIV_OP|FLOAT_DIV_OP|MOD_OP) expr5| expr5;
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        if ctx.getChildCount()==1:
            return ctx.expr5().accept(self)
        else:
            return BinaryOp(ctx.getChild(1).getText(),ctx.expr4().accept(self),ctx.expr5().accept(self))


    # expr5: expr5 CONCAT_OP expr6| expr6;
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        if ctx.getChildCount()==1:
            return ctx.expr6().accept(self)
        else:
            return BinaryOp(ctx.CONCAT_OP().getText(),ctx.expr5().accept(self),ctx.expr6().accept(self))



    # expr6: NOT_OP expr6 |expr7;
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        if ctx.getChildCount()==1:
            return ctx.expr7().accept(self)
        else:
            return UnaryOp(ctx.NOT_OP().getText(),ctx.expr6().accept(self))


    # expr7: (ADD_OP|SUB_OP) expr8 |expr8;
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        if ctx.getChildCount()==1:
            return ctx.expr8().accept(self)
        else:
            return UnaryOp(ctx.getChild(0).getText(),ctx.expr8().accept(self))


    # expr8: expr8 LSB expr RSB |expr9;
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        if ctx.getChildCount()==1:
            return ctx.expr9().accept(self)
        else:
            return ArrayCell(ctx.expr8().accept(self),ctx.expr().accept(self))


    # expr9: expr9 DOT ID (LB expr_lst? RB) |expr9 DOT ID | expr10;
    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        if ctx.getChildCount()==1:
            return ctx.expr10().accept(self)
        elif ctx.getChildCount()==3:
            return FieldAccess(ctx.expr9().accept(self),Id(ctx.ID().getText()))
        else:
            return CallExpr(ctx.expr9().accept(self),Id(ctx.ID().getText()),ctx.expr_lst().accept(self) if ctx.expr_lst()!=None else [])



    # expr10:NEW_LIT ID LB expr_lst? RB| expr11;
    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        if ctx.getChildCount()==1:
            return ctx.expr11().accept(self)
        else:
            return NewExpr(Id(ctx.ID().getText()),ctx.expr_lst().accept(self) if ctx.expr_lst()!=None else [])


    # expr11: ID | INTMT| FLOATMT|STRINGMT |BOOLMT |THIS_LIT|NIL_LIT|LB expr RB|LCB array_value RCB;
    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        if ctx.ID()!=None:
            return Id(ctx.ID().getText())
        elif ctx.INTMT()!=None:
            return IntLiteral(int(ctx.INTMT().getText()))
        elif ctx.FLOATMT()!=None:
            return FloatLiteral(float(ctx.FLOATMT().getText()))
        elif ctx.STRINGMT()!=None:
            return StringLiteral(ctx.STRINGMT().getText())
        elif ctx.BOOLMT()!=None:
            return BooleanLiteral(True if ctx.BOOLMT().getText()=="true" else False)
        elif ctx.THIS_LIT()!=None:
            return SelfLiteral()
        elif ctx.NIL_LIT()!=None:
            return NullLiteral()
        elif ctx.LB()!=None:
            return ctx.expr().accept(self)
        else:
            return ArrayLiteral(ctx.array_value().accept(self))



    # expr_lst:expr COMMA expr_lst| expr;
    def visitExpr_lst(self, ctx:BKOOLParser.Expr_lstContext):
        return [ctx.expr().accept(self)] if ctx.getChildCount()==1 else [ctx.expr().accept(self)] + ctx.expr_lst().accept(self)


    # block_statement:LCB block_decl_lst statement_lst RCB;
    def visitBlock_statement(self, ctx:BKOOLParser.Block_statementContext):
        return Block(ctx.block_decl_lst().accept(self),ctx.statement_lst().accept(self))


    # block_decl_lst: block_decl block_decl_lst|;
    def visitBlock_decl_lst(self, ctx:BKOOLParser.Block_decl_lstContext):
        return ctx.block_decl().accept(self)+ctx.block_decl_lst().accept(self) if ctx.block_decl()!=None else []


    # block_decl: var_decl_2|array_decl_2;
    def visitBlock_decl(self, ctx:BKOOLParser.Block_declContext):
        return ctx.var_decl_2().accept(self) if ctx.var_decl_2()!=None else ctx.array_decl_2().accept(self)


    # statement_lst: statement statement_lst | ;
    def visitStatement_lst(self, ctx:BKOOLParser.Statement_lstContext):
        return [ctx.statement().accept(self)] + ctx.statement_lst().accept(self) if ctx.statement()!=None else []


    # var_decl_2:(FINAL_LIT)? vdecl_type var_lst SEMI;
    def visitVar_decl_2(self, ctx:BKOOLParser.Var_decl_2Context):
        vtype=ctx.vdecl_type().accept(self)
        vlist=ctx.var_lst().accept(self)
        reval=[]
        if ctx.FINAL_LIT()==None:
            for x in vlist:
                if len(x)==1:
                    reval+=[VarDecl(x[0],vtype)]
                elif len(x)==2:
                    reval+=[VarDecl(x[0],vtype,x[1])]
        else:
            reval+=[ConstDecl(x[0],vtype,x[1]) for x in vlist]
        return reval
        #return [VarDecl(x[0],vtype) for x in vlist if len(x)==1 ] + [VarDecl(x[0],vtype,x[1]) for x in vlist if len(x) ==2] if ctx.FINAL_LIT()==None else [ConstDecl(x[0],vtype,x[1]) for x in vlist]


    # array_decl_2:array_type array_lst SEMI;
    def visitArray_decl_2(self, ctx:BKOOLParser.Array_decl_2Context):
        atype=ctx.array_type().accept(self)
        alist=ctx.array_lst().accept(self)
        reval=[]
        if ctx.FINAL_LIT()==None:
            for x in alist:
                if len(x)==1:
                    reval+=[VarDecl(x[0],atype)]
                elif len(x)==2:
                    reval+=[VarDecl(x[0],atype,x[1])]
        else:
            reval+=[ConstDecl(x[0],atype,x[1]) for x in alist]
        return reval
        #return [VarDecl(x[0],atype) for x in alist if len(x)==1] + [VarDecl(x[0],atype,x[1]) for x in alist if len(x)==2] if ctx.FINAL_LIT()==None else [ConstDecl(x[0],atype,x[1]) for x in alist]


    # statement:  block_statement | assign_statement
    #        | if_statement |for_statement
    #        |break_statement| continue_statement 
    #        | return_statement| methodcall_statement ;
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        if ctx.block_statement()!=None:
            return ctx.block_statement().accept(self)
        elif ctx.assign_statement()!=None:
            return ctx.assign_statement().accept(self)
        elif ctx.if_statement()!=None:
            return ctx.if_statement().accept(self)
        elif ctx.for_statement()!=None:
            return ctx.for_statement().accept(self)
        elif ctx.break_statement()!=None:
            return ctx.break_statement().accept(self)
        elif ctx.continue_statement()!=None:
            return ctx.continue_statement().accept(self)
        elif ctx.return_statement()!=None:
            return ctx.return_statement().accept(self)
        else:
            return ctx.methodcall_statement().accept(self)


    # assign_statement: var_name ASSIGN_OP expr SEMI;
    def visitAssign_statement(self, ctx:BKOOLParser.Assign_statementContext):
        return Assign(ctx.var_name().accept(self),ctx.expr().accept(self))

    # var_name: ID | expr DOT ID |expr LSB expr RSB;
    def visitVar_name(self, ctx:BKOOLParser.Var_nameContext):
        if ctx.getChildCount()==1:
            return Id(ctx.ID().getText())
        elif ctx.expr(1)!=None:
            return ArrayCell(ctx.expr(0).accept(self),ctx.expr(1).accept(self))
        else:
            return FieldAccess(ctx.expr(0).accept(self),Id(ctx.ID().getText()))


    # if_statement: IF_LIT expr THEN_LIT statement else_state;
    def visitIf_statement(self, ctx:BKOOLParser.If_statementContext):
        return If(ctx.expr().accept(self),ctx.statement().accept(self),ctx.else_state().accept(self))


    # else_state:ELSE_LIT statement |;
    def visitElse_state(self, ctx:BKOOLParser.Else_stateContext):
        return ctx.statement().accept(self) if ctx.getChildCount()!=0 else None


    # for_statement: FOR_LIT ID ASSIGN_OP expr (TO_LIT|DOWNTO_LIT) expr DO_LIT statement;
    def visitFor_statement(self, ctx:BKOOLParser.For_statementContext):
        return For(Id(ctx.ID().getText()),ctx.expr(0).accept(self),ctx.expr(1).accept(self),ctx.TO_LIT()!=None,ctx.statement().accept(self))


    # break_statement: BREAK_LIT SEMI;
    def visitBreak_statement(self, ctx:BKOOLParser.Break_statementContext):
        return Break()


    # continue_statement: CONT_LIT SEMI;
    def visitContinue_statement(self, ctx:BKOOLParser.Continue_statementContext):
        return Continue()


    # return_statement: RETURN_LIT expr SEMI;
    def visitReturn_statement(self, ctx:BKOOLParser.Return_statementContext):
        return Return(ctx.expr().accept(self))

    # methodcall_statement: expr DOT ID LB expr_lst? RB SEMI ;
    def visitMethodcall_statement(self, ctx:BKOOLParser.Methodcall_statementContext):
        return CallStmt(ctx.expr().accept(self),Id(ctx.ID().getText()),ctx.expr_lst().accept(self) if ctx.expr_lst()!=None else [])