//1913844
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: class_decl_lst EOF;

class_decl_lst: class_decl class_decl_lst| class_decl;

class_decl: CLASS_LIT ID (EXTEND_LIT ID)? LCB decl_lst RCB ;

decl_lst: vm_decl decl_lst | ;

vm_decl : var_decl | method_decl |array_decl; 

//

array_decl: var_decl_pre array_type array_lst SEMI;

array_type:vdecl_type LSB INTMT RSB;

array_lst: array_assign COMMA array_lst| array_assign;

array_assign: ID '=' LCB array_value RCB|ID | ID '=' expr;

array_value: array_val COMMA array_value|array_val;

array_val: BOOLMT|STRINGMT|INTMT|FLOATMT;

//

var_decl:var_decl_pre vdecl_type var_lst SEMI;

var_decl_pre: FINAL_LIT | STATIC_LIT |FINAL_LIT STATIC_LIT |STATIC_LIT FINAL_LIT | ;

vdecl_type: INT_LIT |FLOAT_LIT |BOOL_LIT | STRING_LIT| ID ;

var_lst: var_assign COMMA var_lst| var_assign;

var_assign: ID '=' expr | ID;


//
method_decl:method_decl_pre mdecl_type (ID|MAIN_LIT) LB para_lst? RB block_statement ;

method_decl_pre: STATIC_LIT | ;

para_lst: para_decl SEMI para_lst | para_decl;

para_decl:(vdecl_type|array_type) id_lst;

id_lst: ID COMMA id_lst |ID;

mdecl_type: vdecl_type| array_type|VOID_LIT|;

//COMMENT	

COMMENT: '/*' ( . )*? '*/' ->skip;

LINE_COMMENT: '#' ~('\n'|'\r')* '\r'? '\n' ->skip;

//

expr: expr1 (GREAT_OP|LESS_OP|GEQUA_OP|LEQUA_OP) expr1 |expr1;

expr1: expr2 (ISEQUA_OP|NEQUA_OP) expr2 | expr2 ;

expr2: expr2 (AND_OP| OR_OP) expr3 |expr3;

expr3: expr3 (ADD_OP|SUB_OP) expr4| expr4;

expr4: expr4 (MUL_OP|INT_DIV_OP|FLOAT_DIV_OP|MOD_OP) expr5| expr5;

expr5: expr5 CONCAT_OP expr6| expr6;

expr6: NOT_OP expr6 |expr7;

expr7: (ADD_OP|SUB_OP) expr8 |expr8;

expr8: expr8 LSB expr RSB |expr9;

expr9: expr9 DOT ID (LB expr_lst? RB) |expr9 DOT ID | expr10;

expr10:NEW_LIT ID LB expr_lst? RB| expr11;

expr11: ID | INTMT| FLOATMT|STRINGMT |BOOLMT |THIS_LIT|NIL_LIT|LB expr RB|LCB array_value RCB;

expr_lst:expr COMMA expr_lst| expr;

//

STRINGMT: '"' ( '\\' [bfnrt"\\] | ~["\\\n] )* '"' ;

INTMT: [0-9]+;

FLOATMT: INTMT (DECIMALPT|EXPONENTPT|DECIMALPT EXPONENTPT);

fragment DECIMALPT: DOT [0-9]*;

fragment EXPONENTPT: ('e'|'E') (ADD_OP|SUB_OP)? [0-9]+;

BOOLMT: TRUE_LIT|FALSE_LIT;

//

block_statement:LCB block_decl_lst statement_lst RCB;

block_decl_lst: block_decl block_decl_lst|;

block_decl: var_decl_2|array_decl_2;

statement_lst: statement statement_lst | ;

var_decl_2:(FINAL_LIT)? vdecl_type var_lst SEMI;

array_decl_2:(FINAL_LIT)? array_type array_lst SEMI;

statement:  block_statement | assign_statement
			| if_statement |for_statement
			|break_statement| continue_statement 
			| return_statement| methodcall_statement ;

assign_statement: var_name ASSIGN_OP expr SEMI;

var_name: ID | expr DOT ID |expr LSB expr RSB;

if_statement: IF_LIT expr THEN_LIT statement else_state;

else_state:ELSE_LIT statement |;

for_statement: FOR_LIT ID ASSIGN_OP expr (TO_LIT|DOWNTO_LIT) expr DO_LIT statement;

break_statement: BREAK_LIT SEMI;

continue_statement: CONT_LIT SEMI;

return_statement: RETURN_LIT expr SEMI;

methodcall_statement: expr DOT ID LB expr_lst? RB SEMI ;



//LITERALS

MAIN_LIT: 'main';

INT_LIT: 'int';

FLOAT_LIT: 'float';

VOID_LIT:'void';

BOOL_LIT: 'boolean';

CLASS_LIT: 'class';

FINAL_LIT: 'final';

STATIC_LIT: 'static';

BREAK_LIT: 'break';

CONT_LIT: 'continue';

DO_LIT: 'do';

ELSE_LIT: 'else';

EXTEND_LIT: 'extends';

IF_LIT:'if';

NEW_LIT: 'new';

STRING_LIT: 'string';

THEN_LIT: 'then';

FOR_LIT: 'for';

RETURN_LIT:'return';

TRUE_LIT: 'true';

FALSE_LIT: 'false';

NIL_LIT: 'nil';

THIS_LIT: 'this';

TO_LIT:'to';

DOWNTO_LIT: 'downto';

//
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

//OPERATOR

ADD_OP: '+';

SUB_OP: '-';

MUL_OP: '*';

FLOAT_DIV_OP: '/';

INT_DIV_OP: '\\';

MOD_OP: '%';

NEQUA_OP: '!=';

ISEQUA_OP: '==';

LESS_OP: '<';

GREAT_OP: '>';

LEQUA_OP: '<=';

GEQUA_OP: '>=';

OR_OP: '||';

AND_OP: '&&';

NOT_OP: '!';

CONCAT_OP: '^';

ASSIGN_OP: ':=';

//SEPARATOR

LSB: '[';

RSB: ']';

LCB: '{';

RCB: '}';

LB: '(';

RB: ')';

SEMI: ';';

COLON: ':';

DOT: '.';

COMMA: ',';

//ERROR

WS: [ \f\t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' ( '\\' [bfnrt"\\] | ~["\\] )* ('\n'|EOF)   {raise UncloseString(self.text)};

ILLEGAL_ESCAPE: '"'(~["\\] | '\\' [bfrtn"\\])* ('\\' ~[bfrnt"]) .*?'"' {raise IllegalEscape(self.text)};

