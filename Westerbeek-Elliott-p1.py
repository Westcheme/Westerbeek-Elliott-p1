from sly import Lexer

class Winter2024Lexer(Lexer):
  # define names of tokens
  # KEYWORDS: nothing, int, double, bool, string, class, interface, null, this, extends, implements, for, while, if, else, return, break, new, ArrayInstance, Output, InputInt, InputLine
  # OPERATORS: +  −  ∗  /  %  <  <=  >  >=  =  ==  !=  &&  ||  !  ;  ,  .  [  ]  (   ) {  }
  tokens = {PLUS, MINUS, TIMES, DIVIDE, MOD, LESS, LESSEQUAL, GREATER, GREATEREQUAL, ASSIGN, EQUIVALENT, NOTEQUAL, AND, OR, NOT, SEMICOLON, COMMA, DOT, LEFTBRACKET, RIGHTBRACKET, LEFTPAR, RIGHTPAR, LEFTCURLY, RIGHTCURLY,
            NOTHING, INTK, DOUBLEK, BOOLK, STRINGK, CLASS, INTERFACE, NULL, THIS, EXTENDS, IMPLEMENTS, FOR, WHILE, IF, ELSE, RETURN, BREAK, NEW, ARRAYINSTANCE, OUTPUT, INPUTINT, INPUTLINE,
            INTEGER, DOUBLE, BOOLEAN, STRING, IDENTIFIER}


  # Literals, type and value are the same as the character
  literals = {'+', '-', '*', '/', '%'}
  # Items to ignore
  ignore = ' \t'                      # ignore white space
  ignore_comment1 = '\/\/.*'          # ignore // style comments

  # speficy REs for each token (token group)

  # String
  STRING = r'\"(?:[^"\n])*\"'

  # Special symbols
  LESSEQUAL = r'\<\='
  GREATEREQUAL = r'\>\='
  EQUIVALENT = r'\=\='
  NOTEQUAL = r'\!\='
  LESS = r'\<'
  GREATER = r'\>'
  ASSIGN = r'\='
  AND = r'\&\&'
  OR = r'\|\|'
  NOT = r'\!'
  SEMICOLON = r'\;'
  COMMA = r'\,'
  DOT = r'\.'
  LEFTBRACKET = r'\['
  RIGHTBRACKET = r'\]'
  LEFTPAR = r'\('
  RIGHTPAR = r'\)'
  LEFTCURLY = r'\{'
  RIGHTCURLY = r'\}'

  # Numbers
  DOUBLE = r'[0-9]+\.[0-9]*(E(\+?|\-)[0-9]+)?'
  INTEGER = r'[0-9]+'
  
  # Identifiers
  IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]{0,49}'

  # special case Identifiers
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

  # Multiline comment rule
  @_(r'/\*(.|\n)*?\*/')
  def multiline_comment(self, t):
    self.lineno += t.value.count('\n')

  # Error handling for unterminated multiline comments
  @_(r'/\*(.|\n)*')
  def multiline_comment_error(self, t):
    print (f"Unterminated multiline comment starting at line {self.lineno}")

  # Newline handling
  @_(r'\n+')
  def ignore_newline(self, t):
    self.lineno += t.value.count('\n')

  # Error handling for invalid characters and token
  def error(self, t):
    print ('Invalid character/token: ', t.value[0])
    self.index+= 1


# Loop to enter as much code as you want and run the Lexical Analyzer on that input until terminated
if __name__ =='__main__':
  myscanner = Winter2024Lexer()
  stream = '''

           '''
  while(True):
    stream = input('Enter your DLang Code: ')
    for token in myscanner.tokenize(stream):
      print ('type=%r , value=%r' %(token.type, token.value))
