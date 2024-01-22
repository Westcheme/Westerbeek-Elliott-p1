from sly import Lexer

class Winter2024Lexer(Lexer):
  # define names of tokens
  # KEYWORDS: nothing, int, double, bool, string, class, interface, null, this, extends, implements, for, while, if, else, return, break, new, ArrayInstance, Output, InputInt, InputLine
  # OPERATORS: +  −  ∗  /  %  <  <=  >  >=  =  ==  !=  &&  ||  !  ;  ,  .  [  ]  (   ) {  }
  tokens = {PLUS, MINUS, TIMES, DIVIDE, MOD, LESS, LESSEQUAL, GREATER, GREATEREQUAL, ASSIGN, EQUIVALENT, NOTEQUAL, AND, OR, NOT, SEMICOLON, COMMA, DOT, LEFTBRACKET, RIGHTBRACKET, LEFTPAR, RIGHTPAR, LEFTCURLY, RIGHTCURLY,
            NOTHING, INTK, DOUBLEK, BOOL, STRING, CLASS, INTERFACE, NULL, THIS, EXTENDS, IMPLEMENTS, FOR, WHILE, IF, ELSE, RETURN, BREAK, NEW, ARRAYINSTANCE, OUTPUT, INPUTINT, INPUTLINE,
            INTEGER, DOUBLE, IDENTIFIER}

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
  DOT= r'\.'

  # Numbers
  INTEGER = r'[0-9]+'
  DOUBLE= r'[0-9]+\.[0-9]*'
  
  #DOUBLE = r'[0-9]+\.[0-9]* | [0-9]+\.[0-9]*(E)(\+)?[0-9]'

  # Identifiers
  IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]{0,49}'

  # specisal case for keywords
  #IDENTIFIER['int'] = INTK
  #IDENTIFIER['float'] = FLOATK
  #IDENTIFIER['char'] = CHAR
  IDENTIFIER['bool'] = BOOL
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
            0.45
           '''
    #input('Winter2024Lexer$')
  for token in myscanner.tokenize(stream):
    print ('type=%r , value=%r' %(token.type, token.value))
