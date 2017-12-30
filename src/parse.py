from tokenize import Tokenizer

class ParseError(Exception):
    def __init__(self, line, col, error):
        self.line = line
        self.col = col
        self.error = error

class Structure:
    def __init__(self, type, tokens):
        self.type = type
        self.tokens = tokens

def parse_label(tokens):
    '''Parses a list of tokens into a Label structure'''
    if len(tokens) == 1:
        t = tokens[0]
        raise ParseError(t.line, t.col, 'Missing label name')
    
    if len(tokens) >= 3:
        t = tokens[1]
        raise ParseError(t.line, t.col, 'Label name must be a single word')
    
    if not tokens[0].has_type('word'):
        t = tokens[0]
        raise ParseError(t.line, t.col, 'Invalid label name "{}"'.format(t))
    
    return Structure('label', tokens)

def parse_instruction(tokens):
    '''Parses a list of tokens into an Instruction structure'''
    if len(tokens) == 1:
        return None
    
    if not tokens[0].has_type('word'):
        t = tokens[0]
        raise ParseError(t.line, t.col, 'Invalid instruction name "{}"'.format(t))
    
    return Structure('instruction', tokens)

def parse(tokens):
    '''Parses a list of tokens into a list of assembly language structures'''
    structures = []
    
    current = []
    for tok in tokens:
        current.append(tok)
        if tok.string == ':':
            obj = parse_label(current)
            if obj is not None:
                structures.append(obj)
            current = []
        elif tok.string == '.' or tok.has_type('eol') or tok.has_type('eof'):
            obj = parse_instruction(current)
            if obj is not None:
                structures.append(obj)
            current = []
    
    return structures
