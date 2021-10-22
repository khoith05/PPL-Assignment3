from AST import * 
from Visitor import *
from StaticError import *
from functools import reduce

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

class BKArraytype:
    def __init__(self,size,artype):
        self.artype=artype
        self.size=size
    def isClass(self):
        return isinstance(self.artype,str)
    def __str__(self):
        return "{ size: "+self.size+",type: "+str(self.artype)+"}"
    def __eq__(self,other):
        if isinstance(other,BKArraytype):
            return self.artype==other.artype and self.size==other.size
        else:
            return False

class Var:
    def __init__(self,name,bktype,isStatic,isConstant):
        self.name=name
        self.bktype=bktype
        self.isstatic=isStatic
        self.isconstant=isConstant
    def __str__(self):
        return "{ varname: "+self.name + ",type: "+self.bktype+",Static: "+str(self.isstatic)+",Constant: "+str(self.isconstant)+"}"


class Func:
    def __init__(self,name,bktype,partype,isStatic):
        self.name=name
        self.bktype=bktype
        self.partype=partype
        self.isstatic=isStatic
    def __str__(self):
        return "{ funcname: "+self.name+",rettype: "+(str(self.bktype) if not isinstance(self.bktype,str) else self.bktype)+",para: ["+','.join(str(i) for i in self.partype)+"],Static: "+str(self.isstatic)+"}"

class BKClass(Utils):
    global_envi=[]
    def __init__(self,name,parent,varlst,funclst,construct=None):
        self.name=name
        self.parent=parent
        self.varlst=varlst
        self.funclst=funclst
        self.construct=construct
    def __str__(self):
        return "{ classname: ["+(','.join(str(i) for i in self.name) if isinstance(self.name,list) else self.name)+"],parent: "+self.parent+",\nvarlist: ["+','.join(str(i) for i in self.varlst)+"],\nfunclist: ["+','.join(str(i) for i in self.funclst)+"]}"
    def addClass(self,bkclass):
        self.name+=[bkclass.name]
        self.varlst+=bkclass.varlst
        self.funclst+=bkclass.funclst
    def findAtt(self,Attname):
        findInClass=self.lookup(Attname,self.varlst,lambda x:x.name)
        if findInClass==None:
            parname=self.parent
            while parname!="":
                parclass=self.lookup(parname,BKClass.global_envi,lambda x: x.name)
                if parclass==None:
                    raise Undeclared(Class(),parname)
                findInPar=self.lookup(Attname,parclass.varlst,lambda x: x.name)
                if findInPar!=None:
                    return findInPar
                else:
                    parname=parclass.parent

        else:
            return findInClass
        return None


    def findFunc(self,Funcname):
        findInClass=self.lookup(Funcname,self.funclst,lambda x:x.name)
        if findInClass==None:
            parname=self.parent
            while parname!="":
                parclass=self.lookup(parname,BKClass.global_envi,lambda x: x.name)
                if parclass==None:
                    raise Undeclared(Class(),parname)
                findInPar=self.lookup(Funcname,parclass.funclst,lambda x: x.name)
                if findInPar!=None:
                    return findInPar
                else:
                    parname=parclass.parent

        else:
            return findInClass
        return None

    def isSubclass(self,classname):
        parname=self.parent
        while parname!="":
            if parname==classname:
                return True
            else:
                parclass=self.lookup(parname,BKClass.global_envi,lambda x:x.name)
                parname=parclass.parent
        return False
        
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
        global_envi=c
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
        if ast.returnType is None:
            method_envi=Func("<init>",None,[],False)
        else:
            method_envi=Func(methodname,ast.returnType.accept(self,c),[],ast.kind.accept(self,c))
        paralist=[]
        def checkParam(para):
            rev=para.accept(self,paralist)
            if rev!=None:
                raise Redeclared(Parameter(),rev)
        list(map(checkParam ,ast.param))
        method_envi.partype+=[para[1] for para in paralist]
        if ast.returnType is None:
            c.construct=method_envi
        else:
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
        return BKArraytype(ast.size,ast.eleType.accept(self,c))
    
    def visitClassType(self, ast, c):
        return ast.classname.accept(self,c)
    
    def visitId(self, ast, c):
        return ast.name
    
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
        if ast.elseStmt:
            ast.elseStmt.accept(self,[])
    
    def visitFor(self, ast, c):
        ast.loop.accept(self,[])

class UndeclaredCheck(BaseVisitor,Utils):

    def compare(self,type1,type2,ast,Error):
            if isinstance(type1, BKArraytype) and isinstance(type2, BKArraytype) and type1==type2:
                return True
            if isinstance(type1, FloatType) and isinstance(type2, IntType):
                return True
            if isinstance(type1,str) and isinstance(type2,str) and type1!=type2:
                findtype2=self.lookup(type2,c[1],lambda x:x.name)
                if findtype2.isSubclass(type1):
                    return True 
            if type(type1)!=type(type2):
                raise Error(ast)
            if type1==type2:
                return True
            raise Error(ast)

    def visitProgram(self, ast, c):
        #Check parent undeclared
        def checkClass(bkclass):
            parname=bkclass.parent
            while parname!="":
                findpar=self.lookup(parname,c,lambda x:x.name)
                if findpar==None:
                    raise Undeclared(Class(),parname)
                else:
                    parname=findpar.parent
        list(map(checkClass,c))
        #visit classdecl
        list(map(lambda classdecl:classdecl.accept(self,c),ast.decl))

    
    def visitVarDecl(self, ast, c):
        typedecl=ast.varType.accept(self,c)
        if ast.varInit!=None:
            typevar=ast.varInit.accept(self,c)
            self.compare(typedecl, typevar,ast,TypeMismatchInExpression)
        return Var(ast.variable.name,typedecl,False,False)

    
    def visitConstDecl(self, ast, c):
        #check init
        typedecl=ast.constType.accept(self,c)
        if ast.value:
            typeconst=ast.value.accept(self,c)
            self.compare(typedecl, typeconst,ast,TypeMismatchInConstant)

        return Var(ast.constant.name,typedecl,False,True)
    
    def visitClassDecl(self, ast, c):
        def checkClasstype(classtype):
            if isinstance(classtype,str):
                classname=classtype 
            elif isinstance(classtype,BKArraytype) and classtype.isClass():
                classname=classtype.artype
            else:
                return
            findclass=self.lookup(classname,c,lambda x:x.name)
            if findclass==None:
                raise Undeclared(Class(),classname)
        #get class from global_envi
        this_class=self.lookup(ast.classname.name,c,lambda x:x.name)
        #Check attribute classtype Undeclared
        list(map(checkClasstype,[x.bktype for x in this_class.varlst]))
        #visitmemlist
        memlist=ast.memlist
        list(map(lambda x: x.accept(self,[this_class,c,[]]),memlist))



    def visitStatic(self, ast, c):
        return None
    
    def visitInstance(self, ast, c):
        return None
    
    def visitMethodDecl(self, ast, c):
        def checkClasstype(classtype):
            if isinstance(classtype,str):
                classname=classtype 
            elif isinstance(classtype,BKArraytype) and classtype.isClass():
                classname=classtype.artype
            else:
                return
            findclass=self.lookup(classname,c[1],lambda x:x.name)
            if findclass==None:
                raise Undeclared(Class(),classname)

        #check parameter classtype undeclared
        this_method=self.lookup(ast.name.name,c[0].funclst,lambda x: x.name)
        if this_method==None and ast.name.name=="<init>":
            this_method=c[0].construct 
        list(map(checkClasstype,this_method.partype))
        #check method return type Undeclared
        checkClasstype(this_method.bktype)
        #get parameterlist
        paramlst=list(map(lambda x: x.accept(self,c),ast.param))
        #visit body
        ast.body.accept(self,[c[0],c[1],paramlst,this_method.bktype])

    
    def visitAttributeDecl(self, ast, c):
        ast.decl.accept(self,c)

    def visitBlock(self, ast, c):
        #get var declared list
        varlst=reduce(lambda y,x:[x.accept(self,[c[0],c[1],c[2]+y])]+y,ast.decl,[])
        #visit statements
        def vsStmt(x):
            if isinstance(x, Return):
                x.accept(self,[c[0],c[1],c[2]+varlst,c[3]])
            else:
                x.accept(self,[c[0],c[1],c[2]+varlst])
        list(map(vsStmt,ast.stmt))

    
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
        return BKArraytype(ast.size,ast.eleType.accept(self,c))
    
    def visitClassType(self, ast, c):
        classtype=ast.classname.name 
        if self.lookup(classtype,c[1],lambda x:x.name)==None:
            raise Undeclared(Class(),classtype)
        return classtype
 
    def visitBinaryOp(self, ast, c):
        leftType=ast.left.accept(self,c)
        rightType=ast.right.accept(self,c)
        if ast.op in ["+","-","*","/"]:
            if (type(leftType)==type(rightType) and leftType==rightType ) and isinstance(leftType, IntType) and ast.op!="/":
                return IntType()
            elif leftType in [IntType(),FloatType()] and rightType in [IntType(),FloatType()]:
                return FloatType()
        elif ast.op in ["<",">",">=","<="]:
            if isinstance(leftType, (IntType,FloatType)) and isinstance(rightType, (IntType,FloatType)):
                return BoolType()
        elif ast.op in ["==","!="]:
            if (type(leftType)==type(rightType) and leftType==rightType ) and isinstance(leftType, IntType):
                return BoolType()
            elif (type(leftType)==type(rightType) and leftType==rightType ) and isinstance(leftType, BoolType):
                return BoolType()
        elif ast.op in ["\\","%"]:
            if (type(leftType)==type(rightType) and leftType==rightType ) and isinstance(leftType, IntType):
                return IntType()
        elif ast.op in ["&&","||"]:
            if (type(leftType)==type(rightType) and leftType==rightType ) and isinstance(leftType, BoolType):
                return BoolType()
        elif ast.op=="^":
            if (type(leftType)==type(rightType) and leftType==rightType ) and isinstance(leftType, StringType):
                return StringType()
        raise TypeMismatchInExpression(ast)


    
    def visitUnaryOp(self, ast, c):
        uType=ast.body.accept(self,c)
        if ast.op in ["+","-"]:
            if isinstance(uType, IntType):
                return IntType()
        elif ast.op =="!":
            if isinstance(uType, BoolType):
                return BoolType()
        raise TypeMismatchInExpression(ast)
    
    def visitCallExpr(self, ast, c):
        #check obj kind and get class

        if isinstance(ast.obj,Id) and self.lookup(ast.obj.name,c[1],lambda x:x.name):
            objStatic=True 
            classcalled=self.lookup(ast.obj.name,c[1],lambda x:x.name)
        else:
            objStatic=False
            classcalledType=ast.obj.accept(self,c)
            if isinstance(classcalledType,str):
                classcalled=self.lookup(classcalledType,c[1],lambda x:x.name)
                if classcalled==None:
                    Undeclared(Class(),classcalledType)
            else:
                raise TypeMismatchInExpression(ast)
        #check method Undeclared
        findmethod=self.lookup(ast.method.name,classcalled.funclst,lambda x:x.name)
        if findmethod==None:
            findmethod=classcalled.findFunc(ast.method.name)
            if findmethod==None:
                raise Undeclared(Method(),ast.method.name)
        if findmethod.isstatic!=objStatic:
            raise IllegalMemberAccess(ast)
        if isinstance(findmethod.bktype, VoidType):
            raise TypeMismatchInExpression(ast)
        #get paramlist
        paramlst=list(map(lambda x:x.accept(self,c),ast.param))

        if len(findmethod.partype)!=len(paramlst):
            raise TypeMismatchInExpression(ast)
        lenparam=len(paramlst)
        list(map(self.compare,findmethod.partype,paramlst,[ast for x in range(lenparam)],[TypeMismatchInExpression for x in range(lenparam)]))
        return findmethod.bktype


    
    def visitNewExpr(self, ast, c):
        #get class
        classcalled=self.lookup(ast.classname.name,c[1],lambda x:x.name)
        if classcalled==None:
            raise Undeclared(Class(),ast.classname.name)
        #get param
        paramlst=list(map(lambda x:x.accept(self,c),ast.param))
        if classcalled.construct==None and len(paramlst)==0:
            return ast.classname.name 
        elif classcalled.construct==None and len(paramlst)!=0:
            raise TypeMismatchInExpression(ast)
        elif len(classcalled.construct.partype)!=len(paramlst):
            raise TypeMismatchInExpression(ast)
        lenparam=len(paramlst)
        list(map(self.compare,classcalled.construct.partype,paramlst,[ast for x in range(lenparam)],[TypeMismatchInExpression for x in range(lenparam)]))
        return ast.classname.name

        

    
    def visitId(self, ast, c):
        # findId=self.lookup(ast.name,c[2]+c[0].varlst,lambda x:x.name)
        # if findId==None:
        #     findId=c[0].findAtt(ast.name)
        #     if findId==None:
        #         raise Undeclared(Identifier(),ast.name)
        # return findId.bktype
        ########Phần trên có thể dùng lại
        findId=self.lookup(ast.name,c[2],lambda x:x.name)
        if findId==None:
            raise Undeclared(Identifier(),ast.name)
        return findId.bktype

    
    def visitArrayCell(self, ast, c):
        arrType=ast.arr.accept(self,c)
        idxType=ast.idx.accept(self,c)
        if ast.idx!=IntType():
            raise TypeMismatchInExpression(ast)
        if not isinstance(arrType,BKArraytype):
            raise TypeMismatchInExpression(ast)
        return arrType.artype
    
    def visitFieldAccess(self, ast, c):
        #check static obj
        if isinstance(ast.obj,Id) and self.lookup(ast.obj.name,c[1],lambda x:x.name):
            objStatic=True 
            classcalled=self.lookup(ast.obj.name,c[1],lambda x:x.name)
        else :
            objStatic=False 
            classcalledType=ast.obj.accept(self,c)
            if isinstance(classcalledType,str):
                classcalled=self.lookup(classcalledType,c[1],lambda x:x.name)
                if classcalled==None:
                    Undeclared(Class(),classcalledType)
            else:
                raise TypeMismatchInExpression(ast)
        #check var Undeclared
        findvar= self.lookup(ast.fieldname.name,classcalled.varlst,lambda x:x.name)
        if findvar==None:
            findvar=classcalled.findAtt(ast.fieldname.name)
            if findvar==None:
                raise Undeclared(Attribute(),ast.fieldname.name)
        if findvar.isstatic!=objStatic:
            raise IllegalMemberAccess(ast)
        return findvar.bktype

    
    
    def visitIf(self, ast, c):
        ifType=ast.expr.accept(self,c)
        if ifType!=BoolType():
            raise TypeMismatchInStatement(ast)
        ast.thenStmt.accept(self,c)
        ast.elseStmt.accept(self,c)

    
    def visitFor(self, ast, c):
        idType=ast.id.accept(self,c)
        e1Type=ast.expr1.accept(self,c)
        e2Type=ast.expr2.accept(self,c)
        if not isinstance(idType, IntType) or not isinstance(e1Type, IntType) or not isinstance(e2Type, IntType):
            raise TypeMismatchInStatement(ast)
        ast.loop.accept(self,c)
    
    def visitContinue(self, ast, c):
        return None
    
    def visitBreak(self, ast, c):
        return None
    
    def visitReturn(self, ast, c):
        if ast.expr:
            typere=ast.expr.accept(self,[c[0],c[1],c[2]])
            self.compare(c[3], typere,ast,TypeMismatchInStatement)

    
    def visitAssign(self, ast, c):
        type1=ast.lhs.accept(self,c)
        type2=ast.exp.accept(self,c)
        if isinstance(type1, VoidType):
            raise TypeMismatchInStatement(ast)
        if isinstance(type1, BKArraytype) and isinstance(type2, BKArraytype) and type1==type2:
            return True
        if isinstance(type1, FloatType) and isinstance(type2, IntType):
            return True
        if isinstance(type1,str) and isinstance(type2,str) and type1!=type2:
            findtype2=self.lookup(type2,c[1],lambda x:x.name)
            if findtype2.isSubclass(type1):
                return True 
        if type(type1)!=type(type2):
            raise TypeMismatchInStatement(ast)
        if type1==type2:
            return True
        raise TypeMismatchInStatement(ast)      
    
    def visitCallStmt(self, ast, c):
        if isinstance(ast.obj,Id) and self.lookup(ast.obj.name,c[1],lambda x:x.name):
            objStatic=True 
            classcalled=self.lookup(ast.obj.name,c[1],lambda x:x.name)
        else:
            objStatic=False
            classcalledType=ast.obj.accept(self,c)
            if isinstance(classcalledType,str):
                classcalled=self.lookup(classcalledType,c[1],lambda x:x.name)
                if classcalled==None:
                    Undeclared(Class(),classcalledType)
            else:
                raise TypeMismatchInExpression(ast)
        #check method Undeclared
        findmethod=self.lookup(ast.method.name,classcalled.funclst,lambda x:x.name)
        if findmethod==None:
            findmethod=classcalled.findFunc(ast.method.name)
            if findmethod==None:
                raise Undeclared(Method(),ast.method.name)
        if findmethod.isstatic!=objStatic:
            raise IllegalMemberAccess(ast)
        #get paramlist
        paramlst=list(map(lambda x:x.accept(self,c),ast.param))

        if len(findmethod.partype)!=len(paramlst):
            raise TypeMismatchInExpression(ast)
        lenparam=len(paramlst)
        list(map(self.compare,findmethod.partype,paramlst,[ast for x in range(lenparam)],[TypeMismatchInStatement for x in range(lenparam)]))
    
    def visitIntLiteral(self, ast, c):
        return IntType()
    
    def visitFloatLiteral(self, ast, c):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, c):
        return BoolType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()
    
    def visitNullLiteral(self, ast, c):
        return ast
    
    def visitSelfLiteral(self, ast, c):
        return c[0].name

    def visitArrayLiteral(self, ast, c):
        size= len(ast.value)
        arrType=ast.value[0].accept(self,c)
        def checkArray(ele):
            if arrType!=ele.accept(self,c):
                raise IllegalArrayLiteral(ast)
        list(map(checkArray,ast.value))

class StaticChecker(BaseVisitor,Utils):

    
            
    
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast,[])

    def visitProgram(self,ast, c):
        global_envi = [
    BKClass("io","",[],[
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
        # Redeclared check
        ast.accept(RedeclareCheck(),global_envi)
        # Undeclared check
        BKClass.global_envi=global_envi
        ast.accept(UndeclaredCheck(),global_envi)
        del global_envi
        del BKClass.global_envi




    def visitFuncDecl(self,ast, c): 
        return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
    

    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Method(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    def visitIntLiteral(self,ast, c): 
        return IntType()
    

