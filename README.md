# JOCUR Assembly (8 bit)

## Language

### Syntax

All numbers are integers, and they come in four varieties: decimal (15), binary
(0b1111), octal (0o17), and hexadecimal (0xf). Whitespace is ignored when it
doesn't split up words/numbers.

Each instruction must be followed by a period character, a newline character,
or the end of the file. Each label must be followed by a colon character.

### Instructions

These instructions have direct translations to the machine code.

Instruction | Description                      | Pseudo-code
------------|----------------------------------|-------------
halt        | Halt execution                   | exit
getc        | Get the c flag                   | $r0 = $c
getn        | Get the n flag                   | $r0 = $n
getnn       | Get the nn flag                  | $r0 = $nn
getp        | Get the p flag                   | $r0 = $p
getnp       | Get the np flag                  | $r0 = $np
getz        | Get the z flag                   | $r0 = $z
getnz       | Get the nz flag                  | $r0 = $nz
not x       | Bitwise negation                 | $r0 = ~$x
jump x      | Jump to an address in memory     | $pc = $x
in x        | Read from the input stream       | $r0 = input $x
out x       | Write to the output stream       | print $x
read x      | Read from memory                 | $r0 = mem[$x]
write x     | Write to memory                  | mem[$x] = $r0
and x y     | Bitwise conjunction              | $r0 = $x & $y
or x y      | Bitwise disjunction              | $r0 = $x \| $y
xor x y     | Bitwise exclusive disjunction    | $r0 = $x ^ $y
add x y     | Addition                         | $r0 = $x + $y
sub x y     | Subtraction                      | $r0 = $x - $y
move x y    | Copy a value into a new register | $y = $x
swap x y    | Swap the values in two registers | $y <-> $x
shl c       | Logical shift left               | $r0 = $r0 << c
shr c       | Logical shift right              | $r0 = $r0 >> c
addi c      | Immediate (constant) addition    | $r0 = $r0 + c
lui c       | Set the upper half of a register | $r0 = c << 4
br + c      | Branch forward if true           | $pc = ($r0 == 0) ? ($pc + 1) : ($pc + 2 + c)
br - c      | Branch backward if true          | $pc = ($r0 == 0) ? ($pc + 1) : ($pc - 1 - c)

### Pseudo Instructions

These instructions have indirect translations to machine code. During
compilation, they are replaced with an expansion sequence which is compiled
normally.

Note that square brackets represent the the selection of a subset of bits from
an 8-bit value. For example, if c = b10110010, then c[0:3] = b1011.

Instruction | Description                 | Expansion
------------|-----------------------------|---------------
jump c      | Jump to a constant address  | lui c[0:3]. addi c[4:7]. jump r0
load c      | Load an 8 bit constant      | lui c[0:3]. addi c[4:7]
eq x y      | Equality comparison         | sub x y. getz
ne x y      | Inequality comparison       | sub x y. getnz
lt x y      | Less than comparison        | sub x y. getp
le x y      | Less or equal comparison    | sub x y. getnp
gt x y      | Greater than comparision    | sub x y. getn
ge x y      | Greater or equal comparison | sub x y. getnn

## Architecture

### Description

- 1 program counter register
- 1 instruction register
- 7 flags (c, n, nn, p, np, z, nz)
- 4 general purpose registers (r0, r1, r2, r3)
- up to 256 bytes of memory
- ALU with the following operations:
    - addition
    - subtraction
    - bitwise not
    - bitwise and
    - bitwise or
    - bitwise xor
    - left shift
    - right shift

### Flags

Each flag is set to 0 or 1 after each logical or arithmetic operation
- c (carry): if the result overflows 8 bits
- n (negative): if the result is negative
- nn (non-negative): if the result is not negative
- p (positive): if the result is positive
- np (non-positive): if the result is not positive
- z (zero): if the result is zero
- nz (non-zero): if the result is not zero

### Machine Code

The machine code translations in this table includes variables (x, y, and c)
which represent the corresponding parameters in the instruction.

Instruction | Machine Code
------------|--------------
halt        | 0000 0000
getc        | 0000 0001
getn        | 0000 0010
getnn       | 0000 0011
getp        | 0000 0100
getnp       | 0000 0101
getz        | 0000 0110
getnz       | 0000 0111
not x       | 0000 10xx
jump x      | 0000 11xx
in x        | 0001 00xx
out x       | 0001 01xx
read x      | 0001 10xx
write x     | 0001 11xx
and x y     | 0010 xxyy
or x y      | 0011 xxyy
xor x y     | 0100 xxyy
add x y     | 0101 xxyy
sub x y     | 0110 xxyy
move x y    | 0111 xxyy
swap x y    | 1000 xxyy
shl c       | 1001 0ccc
shr c       | 1001 1ccc
addi c      | 1010 cccc
lui c       | 1011 cccc
br +c       | 110c cccc
br -c       | 111c cccc
