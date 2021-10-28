#
#    c=[thisClass,
#       GlobalEnvi,
#       Varlist,
#       isConstant,
#       isLoop]
#
#
class ConstantCheck(BaseVisitor,Utils):

    def visitProgram(self, ast, c):
        list(map(lambda x:x.accept(self,c),ast.decl ))
    
    def visitVarDecl(self, ast, c):
        return None
    
    def visitConstDecl(self, ast, c):
        IsConstant=ast.varInit.accept(self,c)
        if c[4]!=IsConstant:
            raise IllegalConstantExpression(ast)
    
    def visitClassDecl(self, ast, c):
        list(map(lambda x:x.accept(self,[thisClass,GlobalEnvi,[],False,False]),ast.memlist))
    
    def visitStatic(self, ast, c):
        return None
    
    def visitInstance(self, ast, c):
        return None
    
    def visitMethodDecl(self, ast, c):
        ast.body.accept(self,[thisClass,GlobalEnvi,[],False,False])
    
    def visitAttributeDecl(self, ast, c):
        
        list(map(lambda x:x.accept(self,[thisClass,GlobalEnvi,VarList,IsConstant]),ast.decl))
        
    
    def visitIntType(self, ast, c):
        return None
    
    def visitFloatType(self, ast, c):
        return None
    
    def visitBoolType(self, ast, c):
        return None
    
    def visitStringType(self, ast, c):
        return None
    
    def visitVoidType(self, ast, c):
        return None
    
    def visitArrayType(self, ast, c):
        return None
    
    def visitClassType(self, ast, c):
        return None
    
    def visitBinaryOp(self, ast, c):
        if not (ast.left.accept(self,c) and ast.right.accept(self,c) ):
            return False
        return True
    
    def visitUnaryOp(self, ast, c):
        if not ast.body.accept(self,c):
            return False
        return True
    
    def visitCallExpr(self, ast, c):
        return None
    
    def visitNewExpr(self, ast, c):
        return False
    
    def visitId(self, ast, c):
        VarID=self.lookup()
        return VarID.isConstant
    
    def visitArrayCell(self, ast, c):
        arrIsConstant=self.lookup()
        return arrIsConstant.isConstant
    
    def visitFieldAccess(self, ast, c):pass
        #get ClassCalled
        #Find fieldname in ClassCalled
        #return isConstant
    
    def visitBlock(self, ast, c):pass
        #get Varlst
        #visit stmt
    
    def visitIf(self, ast, c):
        return None
    
    def visitFor(self, ast, c):
        ScalarVar=self.lookup()
        if ScalarVar.isConstant:
            raise CannotAssignToConstant(Assign(ast.id,ast.expr1))
        ast.loop.accept(self,[c[0],c[1],c[2],c[3],True])
    
    def visitContinue(self, ast, c):
        if not c[4]:
            raise BreakContinueNotInLoop(ast)
    
    def visitBreak(self, ast, c):
        if not c[4]:
            raise BreakContinueNotInLoop(ast)
    
    def visitReturn(self, ast, c):
        return None
    
    def visitAssign(self, ast, c):
        lhsIsConstant=ast.lhs.accept(self,c)
        if lhsIsConstant :
            raise CannotAssignToConstant(ast)
    
    
    def visitIntLiteral(self, ast, c):
        return True
    
    def visitFloatLiteral(self, ast, c):
        return True
    
    def visitBooleanLiteral(self, ast, c):
        return True
    
    def visitStringLiteral(self, ast, c):
        return True
    
    def visitNullLiteral(self, ast, c):
        return None
    
    def visitSelfLiteral(self, ast, c):
        return thisClass.classname

    def visitArrayLiteral(self, ast, c):
        return True