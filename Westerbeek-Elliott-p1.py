from sly import Lexer

#1) Ask prof if '.' should be included in literals
#2) Do you want us to implement the error handling strategies in slide 10 of lecture #2?

class Winter2024Lexer(Lexer):
  # define names of tokens
  # KEYWORDS: nothing, int, double, bool, string, class, interface, null, this, extends, implements, for, while, if, else, return, break, new, ArrayInstance, Output, InputInt, InputLine
  # OPERATORS: +  −  ∗  /  %  <  <=  >  >=  =  ==  !=  &&  ||  !  ;  ,  .  [  ]  (   ) {  }
  tokens = {PLUS, MINUS, TIMES, DIVIDE, MOD, LESS, LESSEQUAL, GREATER, GREATEREQUAL, ASSIGN, EQUIVALENT, NOTEQUAL, AND, OR, NOT, SEMICOLON, COMMA, DOT, LEFTBRACKET, RIGHTBRACKET, LEFTPAR, RIGHTPAR, LEFTCURLY, RIGHTCURLY,
            NOTHING, INTK, DOUBLEK, BOOLK, STRINGK, CLASS, INTERFACE, NULL, THIS, EXTENDS, IMPLEMENTS, FOR, WHILE, IF, ELSE, RETURN, BREAK, NEW, ARRAYINSTANCE, OUTPUT, INPUTINT, INPUTLINE,
            INTEGER, DOUBLE, BOOLEAN, STRING, IDENTIFIER}

  literals = {'+', '-', '*', '/'}
  # specify items to ignore
  ignore = ' \t'                                         # ignore white space
  ignore_newline = r'\n+'                                # ignore newlines
  ignore_comment1 = '\/\/.*'                             # // style comments
  ignore_comment2 = '/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/'  # /* style comments

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
  RIGHTPAR = r'\)'
  SEMICOLON = r'\;'
  ASSIGN = r'\='
  DOT = r'\.'

  # Numbers
  DOUBLE = r'[0-9]+\.[0-9]*(E\+?[0-9]+)?'
  INTEGER = r'[0-9]+'
  
  # Identifiers
  IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]{0,49}'

  # specisal case for keywords
  IDENTIFIER['nothing'] = NOTHING
  IDENTIFIER['int'] = INTK
  IDENTIFIER['double'] = DOUBLEK
  IDENTIFIER['bool'] = BOOLK
  IDENTIFIER['True'] = BOOLEAN
  IDENTIFIER['False'] = BOOLEAN
  IDENTIFIER['string'] = STRINGK
  IDENTIFIER['class'] = CLASS
  IDENTIFIER['interface'] = INTERFACE
  IDENTIFIER['null'] = NULL
  IDENTIFIER['this'] = THIS
  IDENTIFIER['extends'] = EXTENDS
  IDENTIFIER['implements'] = IMPLEMENTS
  IDENTIFIER['for'] = FOR
  IDENTIFIER['while'] = WHILE
  IDENTIFIER['if'] = IF
  IDENTIFIER['else'] = ELSE
  IDENTIFIER['return'] = RETURN
  IDENTIFIER['break'] = BREAK
  IDENTIFIER['new'] = NEW
  IDENTIFIER['ArrayInstance'] = ARRAYINSTANCE
  IDENTIFIER['Output'] = OUTPUT
  IDENTIFIER['InputInt'] = INPUTINT
  IDENTIFIER['InputLine'] = INPUTLINE

  

  # Have error handling
  def error(self, t):
    print ('Invalid character/token: ', t.value[0])
    self.index+= 1



if __name__ =='__main__':
  myscanner = Winter2024Lexer()
  stream = '''
            1.5
            1.5E2
            1.5E+2
            1.5+2
            1.5+E2
           '''
  #stream = input('Enter a bunch of code: ')
  for token in myscanner.tokenize(stream):
    print ('type=%r , value=%r' %(token.type, token.value))
