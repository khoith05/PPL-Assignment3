# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_decl_lst.
    def visitClass_decl_lst(self, ctx:BKOOLParser.Class_decl_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_decl.
    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl_lst.
    def visitDecl_lst(self, ctx:BKOOLParser.Decl_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vm_decl.
    def visitVm_decl(self, ctx:BKOOLParser.Vm_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_decl.
    def visitArray_decl(self, ctx:BKOOLParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_lst.
    def visitArray_lst(self, ctx:BKOOLParser.Array_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_assign.
    def visitArray_assign(self, ctx:BKOOLParser.Array_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_value.
    def visitArray_value(self, ctx:BKOOLParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_val.
    def visitArray_val(self, ctx:BKOOLParser.Array_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl.
    def visitVar_decl(self, ctx:BKOOLParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl_pre.
    def visitVar_decl_pre(self, ctx:BKOOLParser.Var_decl_preContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vdecl_type.
    def visitVdecl_type(self, ctx:BKOOLParser.Vdecl_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_lst.
    def visitVar_lst(self, ctx:BKOOLParser.Var_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_assign.
    def visitVar_assign(self, ctx:BKOOLParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_decl.
    def visitMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_decl_pre.
    def visitMethod_decl_pre(self, ctx:BKOOLParser.Method_decl_preContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#para_lst.
    def visitPara_lst(self, ctx:BKOOLParser.Para_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#para_decl.
    def visitPara_decl(self, ctx:BKOOLParser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#id_lst.
    def visitId_lst(self, ctx:BKOOLParser.Id_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mdecl_type.
    def visitMdecl_type(self, ctx:BKOOLParser.Mdecl_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr6.
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr7.
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr8.
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr9.
    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr10.
    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr11.
    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_lst.
    def visitExpr_lst(self, ctx:BKOOLParser.Expr_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_statement.
    def visitBlock_statement(self, ctx:BKOOLParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_decl_lst.
    def visitBlock_decl_lst(self, ctx:BKOOLParser.Block_decl_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_decl.
    def visitBlock_decl(self, ctx:BKOOLParser.Block_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement_lst.
    def visitStatement_lst(self, ctx:BKOOLParser.Statement_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl_2.
    def visitVar_decl_2(self, ctx:BKOOLParser.Var_decl_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_decl_2.
    def visitArray_decl_2(self, ctx:BKOOLParser.Array_decl_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_statement.
    def visitAssign_statement(self, ctx:BKOOLParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_name.
    def visitVar_name(self, ctx:BKOOLParser.Var_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_statement.
    def visitIf_statement(self, ctx:BKOOLParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#else_state.
    def visitElse_state(self, ctx:BKOOLParser.Else_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_statement.
    def visitFor_statement(self, ctx:BKOOLParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_statement.
    def visitBreak_statement(self, ctx:BKOOLParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_statement.
    def visitContinue_statement(self, ctx:BKOOLParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_statement.
    def visitReturn_statement(self, ctx:BKOOLParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodcall_statement.
    def visitMethodcall_statement(self, ctx:BKOOLParser.Methodcall_statementContext):
        return self.visitChildren(ctx)



del BKOOLParser