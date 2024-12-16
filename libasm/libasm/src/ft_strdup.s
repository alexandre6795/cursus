;C function prototype
;char *strdup(const char *s);
;DESCRIPTION
;       The  strdup()  function  returns a pointer to a new string which is a duplicate of the string s.  Memory for
;       the new string is obtained with malloc(3), and can be freed with free(3).
;
;RETURN VALUE
;       On success, the strdup() function returns a pointer to the duplicated string.  It returns NULL  if  insuffi‐
;       cient memory was available, with errno set to indicate the cause of the error.
;Assembly function
;Arguments:
;   -rdi = pointer to the input string
;   -rax = pointer to the new string

section .text
global ft_strdup
extern malloc , ft_strlen, ft_strcpy , __errno_location
ft_strdup:
    ; need len of string
    call ft_strlen
    push rdi ; save rdi
    inc rax 
    mov rdi , rax
    ; allocate memory
    call malloc wrt ..plt
    test rax , rax
    jz .mallocerror
    ; copy string
    mov rdi , rax
    pop rsi
    mov rdi ,rax
    call ft_strcpy
    ret

.mallocerror:
    neg rax
    mov rdi, rax
    call __errno_location wrt ..plt
    mov [rax] , rdi ;
    mov rax , -1
    ret