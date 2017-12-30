import re

class Token:
    def __init__(self, types, string, line=0, col=0):
        self.types = types if isinstance(types, list) else [types]
        self.string = string
        self.line = line
        self.col = col
    
    def __str__(self):
        return self.string
    
    def __repr__(self):
        return 'Token({}, {})'.format(self.types, self.string)
    
    def has_type(self, type):
        return type in self.types

class Tokenizer:
    def __init__(self, token_defs=None):
        self.regs = []
        if token_defs is not None:
            for token_def in token_defs:
                self.add(token_def)
    
    def __repr__(self):
        return 'Tokenizer({})'.format(self.regs)
    
    def add(self, regex, *types):
        '''Add a regular expression for a type of token to the list'''
        self.add([regex, *types])
    
    def add(self, token_def):
        '''Add a regular expression for a type of token to the list'''
        self.regs.append((re.compile(token_def[0]), token_def[1:]))
    
    def tokenize(self, lines):
        '''Returns a list of tokens from a string iterator'''
        tokens = []
        for row, line in enumerate(lines):
            
            # while we haven't finished the line
            col = 0
            while col < len(line):
                
                # check each regex for a match
                matched = False
                for reg, types in self.regs:
                    m = reg.match(line, col)
                    if m is None:
                        continue
                    
                    # got a match!
                    matched = True
                    new_col = m.span()[1]
                    if types != []:
                        tokens.append(Token(types, line[col:new_col], row + 1, col + 1))
                    col = new_col
                    break
                
                # none of the regexes matched
                # add a single character as an unknown token
                if not matched:
                    tokens.append(Token('unknown', line[col:col+1], row + 1, col + 1))
                    col = col + 1
        
        # add an EOF token
        tokens.append(Token('eof', '', row + 2, 0))
        return tokens
