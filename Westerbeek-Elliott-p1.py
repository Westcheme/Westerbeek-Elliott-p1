from sly import Lexer

class Winter2024Lexer(Lexer):
  # define names of tokens
  tokens = {PLUS, MINUS, TIMES, DIVIDE, LEFTPAR,RIGHTPAR, SEMICOLON, ASSIGN, INTEGER, FLOAT,IDENTIFIER, INTK, FLOATK, DOUBLEK, CHAR, FOR, WHILE, IF, BREAK, SWITCH, CLASS, PRIVATE, PUBLIC, STRING}

  literals ={'+', '-', '*', '/'}
  # specify items to ignore
  ignore = ' \t' # ignore white space
  ignore_newline = r'\n+' # ignore newlines
  ignore_comment1 = '\/\/.*'  # // comment goes here

  # speficy REs for each token (token group)

  # String
  STRING = r'\"(.)*\"'

  # start with keywords
  #INTK ='int'
  #FLOATK='float'
  #CHAR='char'
  #FOR = 'for'
  #WHILE = 'while'
  #IF = 'if'
  #BREAK = 'break'
  #SWITCH = 'switch'
  #CLASS = 'class'
  #PRIVATE ='private'
  #PUBLIC = 'public'

  # Operators
  #PLUS = r'\+'
  #MINUS =r'\-'
  #TIMES =r'\*'
  #DIVIDE =r'\/'

  # Special symbols
  LEFTPAR = r'\('
  RIGHTPAR =r'\)'
  SEMICOLON = r'\;'
  ASSIGN= r'\='

  # Numbers
  FLOAT= r'[0-9]*\.[0-9]+'
  INTEGER = r'[0-9]+'

  # Identifiers
  IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

  # specisal case for keywords
  IDENTIFIER['int'] = INTK
  IDENTIFIER['float'] = FLOATK
  IDENTIFIER['char'] = CHAR
  IDENTIFIER['for'] = FOR
  IDENTIFIER['while'] = WHILE
  IDENTIFIER['if'] = IF
  IDENTIFIER['break'] = BREAK





  # Have error handling
  def error(self, t):
    print ('Invalid character/token: ', t.value[0])
    self.index+= 1



if __name__ =='__main__':
  myscanner = Winter2024Lexer()
  stream = '''
            int x;
            ind y;
            float z;
            w = (x+y*z)/100;
           '''
    #input('Winter2024Lexer$')
  for token in myscanner.tokenize(stream):
    print ('type=%r , value=%r' %(token.type, token.value))
