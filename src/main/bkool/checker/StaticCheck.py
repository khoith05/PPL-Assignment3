from AST import * 
from Visitor import *
from StaticError import *

class Utils:
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None


class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value


# class Arraytype:
#     def __init__(self,btype,size=0):
#         self.btype=btype
#         self.size=size
#     def isArray():
#         return size!=0

class Var:
    def __init__(self,name,bktype,isStatic,isConstant):
        self.name=name
        self.bktype=bktype
        self.isstatic=isStatic
        self.isconstant=isConstant
    def __str__(self):
        return "{ varname: "+self.name + ",type: "+self.bktype+",Static: "+self.isStatic+",Constant: "+self.isconstant+"}"


class Func:
    def __init__(self,name,bktype,partype,isStatic):
        self.name=name
        self.bktype=bktype
        self.partype=partype
        self.isstatic=isStatic
    def __str__(self):
        return "{ funcname: "+self.name+",rettype: "+self.bktype+",para: "+self.partype+",Static: "+self.isstatic+"}"

class BKClass:
    def __init__(self,name,parent,varlst,funclst):
        self.name=name
        self.parent=parent
        self.varlst=varlst
        self.funclst=funclst
    def __str__(self):
        return "{ classname: "+self.name+",parent: "+self.parent+",\nvarlist: "+self.varlst+",\nfunclist: "+self.funclst+"}"
'''
var= {
    "name":str,
    "type":,
    "size":0,
    "kind":
}
func={
    "name":,
    "rettype":,
    "retsize":0,
    "partype":,
    "kind":
}
class={
    "name":,
    "parent":,
    "varlst":,
    "funclst":
}
global=[classlst]
'''

class RedeclareCheck(BaseVisitor):
    
    def visitProgram(self, ast, c):
        global_envi=[]
        # def checkclassdecl(classdecl):
        #     global_envi+=classdecl.accept(self,global_envi)
        list(map(lambda classdecl:classdecl.accept(self,global_envi),ast.decl))
        return global_envi
    
    def visitVarDecl(self, ast, c):
        #get var name
        varname=ast.variable.accept(self,c)
        vartype=ast.varType.accept(self,c)
        #check redeclared
        if varname in [var[0] for var in c] :
            return varname
        #add var 
        c+=[[varname,vartype]]
        return None

    
    def visitConstDecl(self, ast, c):
        #get const name
        constname=ast.constant.accept(self,c)
        consttype=ast.constType.accept(self,c)
        #check redeclared
        if constname in [var[0] for var in c]:
            return constname
        c+=[[constname,consttype]]
        return None
    
    def visitClassDecl(self, ast, c):
        #get class name
        memlist=ast.memlist if isinstance(ast.memlist,list) else ast.parentname
        classname=ast.classname.accept(self,c)
        parent=ast.parentname.accept(self,c) if  ast.parentname and isinstance(ast.parentname,Id)  else "" if ast.parentname==None else ast.memlist.accept(self,c) 
        # check redeclared class
        if classname in [eclass.name for eclass in c]:
            raise Redeclared(Class(),classname)
        #visit class
        class_envi=BKClass(classname,parent,[],[])
        list(map(lambda mem: mem.accept(self,class_envi),memlist))
        c+=[class_envi]
    
    def visitStatic(self, ast, c):
        return True
    
    def visitInstance(self, ast, c):
        return False
    
    def visitMethodDecl(self, ast, c):
        #get method info
        methodname=ast.name.accept(self,c)
        rettype=ast.returnType.accept(self,c) if ast.returnType else None
        #check redeclared method
        if methodname in [efunc.name for efunc in c.funclst]+[evar.name for evar in c.varlst]:
            raise Redeclared(Method() if rettype else SpecialMethod(),methodname)
        #add method into class_envi
        method_envi=Func(methodname,ast.returnType.accept(self,c),[],ast.kind.accept(self,c))
        paralist=[]
        def checkParam(para):
            rev=para.accept(self,paralist)
            if rev!=None:
                raise Redeclared(Parameter(),rev)
        list(map(checkParam ,ast.param))
        method_envi.partype+=[para[1] for para in paralist]
        c.funclst+=[method_envi]
        ast.body.accept(self,paralist)



    
    def visitAttributeDecl(self, ast, c):
        #check redeclared
        varlst=[[var.name,var.bktype] for var in c.varlst]
        rev=ast.decl.accept(self,varlst)
        if rev!=None:
            raise Redeclared(Attribute(),rev)
        attr=Var(varlst[len(varlst)-1][0],varlst[len(varlst)-1][1],ast.kind.accept(self,c),isinstance(ast.decl,ConstDecl))
        c.varlst+=[attr]

    
    def visitIntType(self, ast, c):
        return IntType()
    
    def visitFloatType(self, ast, c):
        return FloatType()
    
    def visitBoolType(self, ast, c):
        return BoolType()
    
    def visitStringType(self, ast, c):
        return StringType()
    
    def visitVoidType(self, ast, c):
        return VoidType()
    
    def visitArrayType(self, ast, c):
        return ArrayType(ast.size,ast.eleType)
    
    def visitClassType(self, ast, c):
        return ast.classname.accept(self,c)
    
    def visitBinaryOp(self, ast, c):
        return None
    
    def visitUnaryOp(self, ast, c):
        return None
    
    def visitCallExpr(self, ast, c):
        return None
    
    def visitNewExpr(self, ast, c):
        return None
    
    def visitId(self, ast, c):
        return ast.name
    
    def visitArrayCell(self, ast, c):
        return None
    
    def visitFieldAccess(self, ast, c):
        return None
    
    def visitBlock(self, ast, c):
        #check redeclared
        def checkDecl(decl):
            rev=decl.accept(self,c)
            if rev!=None:
                raise Redeclared(Variable() if isinstance(decl,VarDecl) else Constant(),rev)
        list(map(checkDecl,ast.decl))
        list(map(lambda stmt: stmt.accept(self,[]),ast.stmt))


    
    def visitIf(self, ast, c):
        ast.thenStmt.accept(self,[])
        ast.elseStmt.accept(self,[])
    
    def visitFor(self, ast, c):
        ast.loop.accept(self,[])
    
    def visitContinue(self, ast, c):
        return None
    
    def visitBreak(self, ast, c):
        return None
    
    def visitReturn(self, ast, c):
        return None
    
    def visitAssign(self, ast, c):
        return None
    
    def visitCallStmt(self, ast, c):
        return None
    
    def visitIntLiteral(self, ast, c):
        return None
    
    def visitFloatLiteral(self, ast, c):
        return None
    
    def visitBooleanLiteral(self, ast, c):
        return None
    
    def visitStringLiteral(self, ast, c):
        return None
    
    def visitNullLiteral(self, ast, c):
        return None
    
    def visitSelfLiteral(self, ast, c):
        return None 

    def visitArrayLiteral(self, ast, c):
        return None 

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    BKClass("io",None,[],[
        Func("readInt",IntType(),[],True),
        Func("writeInt",VoidType(),[IntType()],True),
        Func("writeIntLn",VoidType(),[IntType()],True),
        Func("readFloat",FloatType(),[],True),
        Func("writeFloat",VoidType(),[FloatType()],True),
        Func("writeFloatLn",VoidType(),[FloatType()],True),
        Func("readBool",BoolType(),[],True),
        Func("writeBool",VoidType(),[BoolType()],True),
        Func("writeBoolLn",VoidType(),[BoolType()],True),
        Func("readStr",StringType(),[],True),
        Func("writeStr",VoidType(),[StringType()],True),
        Func("writeStrln",VoidType(),[StringType()],True),])
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast,[])

    def visitProgram(self,ast, c): 
        global_class=ast.accept(RedeclareCheck(),StaticChecker.global_envi)
        StaticChecker.global_envi+=global_class




    def visitFuncDecl(self,ast, c): 
        return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
    

    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    def visitIntLiteral(self,ast, c): 
        return IntType()
    

