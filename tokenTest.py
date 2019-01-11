#---------#---------#---------#---------#---------#--------#
import ply.lex

tokens = [ 'ID', 'INTEGER', 'REAL', 'STRING', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'ASSIGN', 'AT', 'COLON', 'COMMA', 'EQ', 'GE', 'GT',
'LPAREN', 'RPAREN', 'LBRACE', 'LBRACKET', 'LT', 'LE', 'NE', 'PERIOD', 'PTR', 'RBRACE', 'RBRACKET', 'SEMICOLON']

reserved = {
    'while' : 'WHILE', 'then' : 'THEN', 'and' : 'AND', 'by' : 'BY', 'const' : 'CONST', 'div' : 'DIV', 'do' : 'DO', 'elif' : 'ELIF', 'else' : 'ELSE',
    'exit' : 'EXIT', 'extends' : 'EXTENDS', 'for' : 'FOR', 'func' : 'FUNC', 'if' : 'IF', 'loop' : 'LOOP', 'mod' : 'MOD', 'next' : 'NEXT', 'not' : 'NOT',
    'of' : 'OF', 'or' : 'OR', 'read' : 'READ', 'record' : 'RECORD', 'return' : 'RETURN', 'to' : 'TO', 'var' : 'VAR', 'write' : 'WRITE',
}

tokens += reserved.values()

t_INTEGER = r'\d+'
t_REAL = r'(\d+)[.](\d+)[eE]?[+-]?\d+'
t_STRING = r'(")[ a-zA-Z0-9]*(")'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_ASSIGN = r'='
t_AT = r'@'
t_COLON = r':'
t_COMMA = r','
t_EQ = r'=='
t_GE = r'>='
t_GT = r'>'
t_LE = r'<='
t_LT = r'<'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_PERIOD = r'\.'
t_PTR = r'\->'
t_SEMICOLON = r';'
t_WHILE = r'WHILE'
t_AND = r'AND'

# Ignored characters
t_ignore = ' \t'

# Eats characters from the # character to the of the input.

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value,'ID')    # Check for reserved words
  return t

def t_comment(t):
  r'//[^\n]*'
  pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print('Illegal character "%s" on line' % t.value[0], t.lineno)
    t.lexer.skip(1)

def find_column(token, input):
  line_start = input.rfind('\n', 0, token.lexpos) + 1
  return (token.lexpos - line_start) + 1


#---------#---------#---------#---------#---------#--------#
def _main( inputFile ) :
  with open( inputFile, 'r' ) as fp :
    data = fp.read()

  lexer = ply.lex.lex()
  lexer.input( data )

  for token in lexer :
    print("({0}, {1}, {2}, '{3}', '{4}')"
      .format(token.lexpos-1, token.lineno, find_column(token, data), token.type, token.value))

#---------#---------#---------#
if __name__ == '__main__' :
  import sys

  if len( sys.argv ) > 1 :
    _main( sys.argv[ 1 ] )

  else :
    print( 'Input file name required.' )

#---------#---------#---------#---------#---------#--------#
