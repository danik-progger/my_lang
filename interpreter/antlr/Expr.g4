grammar Expr;
SPACES
 : [ \t] -> skip
 ;
FUN: 'fun';
MAIN: 'main';
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
PRINT   : 'print ' ;
IF : 'if ' ;
ELSE: 'else' ;
WHILE : 'while';
IDENT   : [a-zA-Z]+ ;


prog:  FUN MAIN '(' ')' '{' NEWLINE ((stmt NEWLINE)*) '}'
    ;
stmt: PRINT '(' printexp=expr ')'
    | IF exp=expr '{' NEWLINE ((stmt NEWLINE)*) '}'
    | ident=IDENT ('=') assign=expr
    ;
expr:   expr op=('*'|'/') expr // MulExpression | DivExpression # left - .expr(0)
    |   expr op=('+'|'-') expr // AddExpression | SubExpression
    |   value=INT // NumberExpression
    |   '(' exp=expr ')' // BraceExpression
    |   ident=IDENT // IdentExpression
    ;