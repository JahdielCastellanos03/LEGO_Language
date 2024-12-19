// LEGO Grammar
grammar LEGO;

// Lexer Rules
LEGO_INICIO: 'LEGO_INICIO';
LEGO_FIN: 'LEGO_FIN';
MOSTRAR_LEGO: 'MOSTRAR_LEGO';
PEDIR_LEGO: 'PEDIR_LEGO';

//CONDICIONES
SI: 'SI';
SINO: 'SINO';

//ESTRUCTURAS DE CONTROL
REPETIR_LEGO: 'REPETIR_LEGO';
MIENTRAS_APILO: 'MIENTRAS_APILO';

//OPERADORES
AGREGAR_BLOQUE: 'AGREGAR_BLOQUE';
QUITAR_BLOQUE: 'QUITAR_BLOQUE';
APILAR_BLOQUES: 'APILAR_BLOQUES';
DIVIDIR_BLOQUES: 'DIVIDIR_BLOQUES';
POTENCIAR_BLOQUES: 'POTENCIAR_BLOQUES';

//OPERADORES COMPARADORES
MAS_GRANDE_QUE: 'MAS_GRANDE_QUE';
MAS_PEQUE_QUE: 'MAS_PEQUE_QUE';
ESTE_BLOQUE_IGUAL_A: 'ESTE_BLOQUE_IGUAL_A';
DIFERENTE_A: 'DIFERENTE_A';

//GRAMMAR Y TOKENS
BLOQUE_ABRIR: '{';
BLOQUE_CERRAR: '}';
NUMBER: [0-9]+;
IDENTIFICADOR: [a-zA-Z_][a-zA-Z0-9_]*;
PALABRA_BLOQUE: '"' .*? '"';
MUCHOS_BLOQUES: '[' (NUMBER (',' NUMBER)*)? ']';
WS: [ \t\r\n]+ -> skip;
LPAREN: '(';
RPAREN: ')';
EQUAL: '=';
SEMICOLON: ';';
COLON: ':';

// Parser Rules
programa: LEGO_INICIO bloque LEGO_FIN;
bloque: BLOQUE_ABRIR instruccion* BLOQUE_CERRAR;
instruccion: asignacionInstruccion | mostrarInstruccion | pedirInstruccion | condicionInstruccion  | repetirInstruccion | mientrasApiloInstruccion | operacionInstruccion;

asignacionInstruccion: IDENTIFICADOR EQUAL expresion SEMICOLON;
mostrarInstruccion: MOSTRAR_LEGO LPAREN (PALABRA_BLOQUE | IDENTIFICADOR) RPAREN SEMICOLON;
pedirInstruccion: PEDIR_LEGO LPAREN PALABRA_BLOQUE COLON IDENTIFICADOR RPAREN SEMICOLON;
repetirInstruccion: REPETIR_LEGO LPAREN expresion RPAREN bloque;
condicionInstruccion: SI LPAREN condicion RPAREN bloque (SINO bloque)?;
mientrasApiloInstruccion: MIENTRAS_APILO LPAREN condicion RPAREN bloque;
operacionInstruccion: IDENTIFICADOR EQUAL operadorMat SEMICOLON;

expresion: term (operadorMat term)*;
term: factor (operadorMat factor)*;
factor: NUMBER | IDENTIFICADOR | LPAREN expresion RPAREN;

condicion: expresion operadorLog expresion;
operadorLog: MAS_GRANDE_QUE | MAS_PEQUE_QUE | ESTE_BLOQUE_IGUAL_A | DIFERENTE_A;
operadorMat: AGREGAR_BLOQUE | QUITAR_BLOQUE | APILAR_BLOQUES | DIVIDIR_BLOQUES | POTENCIAR_BLOQUES;