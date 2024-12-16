; C function prototype
; size_t strlen(const char *str)
;DESCRIPTION
;       The strlen() function calculates the length of the string pointed to by
;       s, excluding the terminating null byte ('\0').
;
;RETURN VALUE
;       The strlen() function returns the number of bytes in the string pointed
;      to by s.
;Assembly function
; Arguments:
;   -rdi = pointer to the input string first register arugment in x86_64
;   -rax =  length of the string  and return value in x86_64
;
section .text

global ft_strlen ; global declaration for linker know how to link and find start point
; and also for other file to use this function

ft_strlen:
    ; initialize counter to 0
    xor rax, rax ; xor (v1,v1) always return 0

.loop_count:
    ; count the number of iteration until reach NULL character ('\0')
    cmp byte [rdi+ rax], 0 ; compare the value of rdi + rax with 0 (byte by byte)
    ;while( *(str + i) != '\0')
    je .end_count ; if the value is 0, then return the counter
    inc rax ; increment the counter (counter and return have the same register)
    jmp .loop_count ; jump to the loop

.end_count:
    ret ; return the counter value (rax is always the return value in x86_64)