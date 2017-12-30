from parse import Parser

TODO = 0

class VirtualMachineWarning(Exception):
    TODO

class VirtualMachineError(Exception):
    TODO

class VirtualMachine:
    
    FLAGS = 7
    REGS = 4
    MEM = 256
    
    def __init__(self):
        self.initial = []
        self.reset()
    
    def __str__(self):
        TODO
    
    def __repr__(self):
        return self.__str__()
    
    def load(initial):
        '''Load machine code into this virtual machine'''
        size = len(initial)
        if size > MEM:
            raise VirtualMachineError('Cannot load more than {} bytes of data'.format(MEM))
        
        self.initial = initial
        for i in range(0, size):
            self.mem[i] = initial[i]
        for i in range(size, MEM):
            self.mem[i] = 0
    
    def reset(self):
        '''Reset this virtual machine to its initial state from the last time
        data was loaded into it'''
        self.pc = 0
        self.ir = 0
        self.flags = [0] * FLAGS
        self.regs = [0] * REGS
        self.mem = [0] * MEM
        self.load(self.initial)
    
    def step(self):
        '''Execute a single machine instruction'''
        TODO
    
    def run(self):
        '''Run continuously'''
        TODO

def main(args):
    TODO

if __name__ == '__main__':
    from sys import argv
    exit(main(argv[1:]))
