
str:
    data "Hello world!"
    data 0

loop:
    read r1
    move r0 r2
    getz
    br end
    out r2
    move r1 r0
    addi 1
    move r0 r1
    br loop
end:
    halt
