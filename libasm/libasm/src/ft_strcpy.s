; C function prototype 
; char *strcpy(char *dest, const char *src)
;DESCRIPTION
    ;The  strcpy()  function  copies the string pointed to by src, including
    ;the terminating null byte ('\0'), to the buffer  pointed  to  by  dest.
;RETURN VALUE
       ;The strcpy() and strncpy() functions return a pointer to  the  destina‐
       ;tion string dest.
;Assembly function
;Arguments: 
    ;-rdi = pointer to dest string
    ;-rsi = pointer to src string
    ;-rax = pointer to return value
section .text
global ft_strcpy ;
ft_strcpy:

push rdi
.loop:
    mov al ,[rsi] ; move the value of rsi in al
    cmp byte al, 0 ; compare the value of rsi with 0 (byte by byte)
    je .end ; if the value is 0, then return the counter
    mov [rdi], al ; copy rsi value in rdi
    inc rdi
    inc rsi 
    jmp .loop 
.end:
    mov byte [rdi], 0 ; add null terminator
    pop rax
    ret