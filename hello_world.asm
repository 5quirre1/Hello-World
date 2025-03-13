section .data
    msg db "Hello World!", 0Ah
    len equ $ - msg

section .text
    global _start                 ; declare the entry point of the program

_start:
    ; write the message
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    ; exit
    mov rax, 60
    xor rdi, rdi
    syscall
