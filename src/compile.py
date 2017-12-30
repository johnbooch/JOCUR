from parse import Structure

TODO = 0

# JOCUR assembly tokens for tokenization module
ASM_TOKENS = [
    ['#.*'],
    ['[ \t]+'],
    ['\n', 'eol'],
    ['"(\\"|[^"])*"', 'string'],
    ['[_a-zA-Z][_a-zA-Z0-9]*', 'word'],
    ['[0-9]+', 'integer', 'decimal'],
    ['|0?b[01]+', 'integer', 'binary'],
    ['|0?o[0-7]+', 'integer', 'octal'],
    ['0?x[0-9a-fA-F]+', 'integer', 'hex'],
    ['.', 'symbol']
]

# Type 0 Instructions
T0_INSTRS = {
    'halt':  0b00000000,
    'getc':  0b00000001,
    'getn':  0b00000010,
    'getnn': 0b00000011,
    'getp':  0b00000100,
    'getnp': 0b00000101,
    'getz':  0b00000110,
    'getnz': 0b00000111
}

# Type 1 Instructions
T1_INSTRS = {
    'not':   0b00001000,
    'jump':  0b00001100,
    'in':    0b00010000,
    'out':   0b00010100,
    'read':  0b00011000,
    'write': 0b00011100
}

# Type 2 Instructions
T2_INSTRS = {
    'and':   0b00100000,
    'or':    0b00110000,
    'xor':   0b01000000,
    'add':   0b01010000,
    'sub':   0b01100000,
    'move':  0b01110000,
    'swap':  0b10000000
}

# Type 3 Instructions
T3_INSTRS = {
    'shl':   0b10010000,
    'shr':   0b10011000
}

# Type 4 Instructions
T4_INSTRS = {
    'addi':  0b10100000,
    'lui':   0b10110000
}

# Type 5 Instructions
T5_INSTRS = {
    'br':    0b11000000
}

# Type 0 Pseudo Instructions
P0_INSTRS = {
    'jump',
    'load'
}

# Type 1 Pseudo Instructions
P1_INSTRS = {
    'eq',
    'ne',
    'lt',
    'le',
    'gt',
    'ge'
}

class CompileError(Exception):
    def __init__(self, line, col, error):
        self.line = line
        self.col = col
        self.error = error

def get_data(token):
    '''Returns the memory values defined by a data instruction'''
    pass

def parse_integer(token):
    if token.has_type('integer'):
        if token.has_type('decimal'):
            return int(token.string)
        elif token.has_type('binary'):
            return int(token.string, 2)
        elif token.has_type('octal'):
            return int(token.string, 8)
        elif token.has_type('hex'):
            return int(token.string, 16)
    else:
        return None

def parse_register(token):
    if token.has_type('word'):
        if token.string == 'r0':
            return 0
        elif token.string == 'r1':
            return 1
        elif token.string == 'r2':
            return 2
        elif token.string == 'r3':
            return 3
    else:
        return None

def expand(structs):
    '''Expands all pseudo instructions into normal instructions. Returns a
    list of parser Structures'''
    
    expanded = []
    
    for struct in structs:
        name = struct.tokens[0]
        if struct.type == 'instruction' and name.string in P0_INSTRS:
            if len(struct.tokens) < 3:
                raise CompileError(0, 0, 'Too few arguments')
            if len(struct.tokens) > 3:
                raise CompileError(0, 0, 'Too many arguments')
            
            arg = struct.tokens[1]
            
            if name.string == 'jump':
                TODO
                # expanded.push(...)
                # expanded.push(...)
                # expanded.push(...)
                
            elif name.string == 'load':
                TODO
                
        elif struct.type == 'instruction' and name.string in P1_INSTRS:
            if len(struct.tokens) < 4:
                raise CompileError(0, 0, 'Too few arguments')
            if len(struct.tokens) > 4:
                raise CompileError(0, 0, 'Too many arguments')
            
            arg1 = struct.tokens[1]
            arg2 = struct.tokens[2]
            
            if name.string == 'eq':
                TODO
                
            elif name.string == 'ne':
                TODO
                
            elif name.string == 'lt':
                TODO
                
            elif name.string == 'le':
                TODO
                
            elif name.string == 'gt':
                TODO
                
            elif name.string == 'ge':
                TODO
                
        else:
            expanded.append(struct)

def compile(structs):
    '''Compiles a list of structs into machine code'''
    mem = []
    
    labels = {}
    data_segment = True
    for struct in structs:
        if struct.type == 'instruction':
            name = struct.tokens[0]
            if data_segment and name.string == 'data':
                
                # parse a data instruction
                if len(struct.tokens) < 2:
                    raise CompileError(name.line, name.col, 'Missing data definition')
                
                if len(struct.tokens) > 2:
                    raise CompileError(name.line, name.col, 'Too many data definitions')
                
                mem.extend(get_data(struct.tokens[1]))
                continue
            else:
                data_segment = False
                
                # parse a regular instruction
                if name.string in T0_INSTRS:
                    TODO
                    
                elif name.string in T1_INSTRS:
                    TODO
                    
                elif name.string in T2_INSTRS:
                    TODO
                    
                elif name.string in T3_INSTRS:
                    TODO
                    
                elif name.string in T4_INSTRS:
                    TODO
                    
                elif name.string in T5_INSTRS:
                    TODO
                    
                elif name.string == 'data':
                    raise CompileError(name.line, name.col, 'Data value defined after data segment')
            
        elif struct.type == 'label':
            TODO
