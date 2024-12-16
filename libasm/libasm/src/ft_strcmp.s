;C fonction prototype
;int strcmp(const char *s1, const char *s2);
;
;DESCRIPTION
       ;The strcmp() function compares the two strings s1 and s2.  The locale is not taken into account (for a locale-aware comparison, see strcoll(3)).  The comparison is done using unsigned characters.

       ;strcmp() returns an integer indicating the result of the comparison, as follows:

      ; • 0, if the s1 and s2 are equal;

       ;• a negative value if s1 is less than s2;

      ; • a positive value if s1 is greater than s2.

      ; The strncmp() function is similar, except it compares only the first (at most) n bytes of s1 and s2.
;
;RETURN VALUE
       ;The strcmp() and strncmp() functions return an integer less than, equal to, or greater than zero if s1 (or the first n bytes thereof) is found, respectively, to be less than, to match, or be greater than s2.
;Assembly function
;Arguments:

    ;rdi s1(char*)
    ;rsi s2(char*)
    ;rax return value (int)
;
section .text
global ft_strcmp
ft_strcmp:
 .loop:
    mov al ,[rdi] ;move the value of rdi in al
    mov bl ,[rsi] ;move the value of rsi in bl
    cmp al, bl ;compare al and bl
    jne .not_equal ;if not equal jump to .notequal
    test al , al ;test if al is null
    ; cmp al, 0 compare al with 0 work too but test is more efficient and more readable
    je .end ; if al is null end the loop
    inc rdi ;increment rdi
    inc rsi ;increment rsi
    jmp .loop ;jump to the loop 

.not_equal:
    sub al , bl ;substract al and bl (ASCII VALUE)
    movsx rax , al ;move the result in rax movsx sign extend the result
    ret ;return the result
.end:
     xor rax, rax ;initialize rax to 0
    ret ;return 0