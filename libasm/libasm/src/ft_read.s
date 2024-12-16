;ssize_t read(int fd, void *buf, size_t count);

;DESCRIPTION
;       read()  attempts to read up to count bytes from file descriptor fd into
;       the buffer starting at buf.

;       On files that support seeking, the read operation commences at the file
;       offset, and the file offset is incremented by the number of bytes read.
;       If the file offset is at or past the end of file, no  bytes  are  read,
;       and read() returns zero.

;       If count is zero, read() may detect the errors described below.  In the
;       absence of any errors, or if read() does not check for errors, a read()
;       with a count of 0 returns zero and has no other effects.

;       According to POSIX.1, if count is greater than SSIZE_MAX, the result is
;       implementation-defined; see NOTES for the upper limit on Linux.

;RETURN VALUE
;       On success, the number of bytes read is returned (zero indicates end of
;       file),  and the file position is advanced by this number.  It is not an
;       error if this number is smaller than the  number  of  bytes  requested;
;       this  may happen for example because fewer bytes are actually available
;       right now (maybe because we were close to end-of-file,  or  because  we
;       are reading from a pipe, or from a terminal), or because read() was in‐
;       terrupted by a signal.  See also NOTES.

;       On error, -1 is returned, and errno  is  set  appropriately.   In  this
;       case,  it  is  left  unspecified  whether  the  file  position (if any)
;       changes.

;Assembly function
;Arguments:
;   -rdi = file descriptor
;   -rsi = pointer to buffer
;   -rdx = number of bytes to read
;   -rax = number of bytes read

section .text
global ft_read
extern __errno_location 

ft_read:
    mov rax, 0
    syscall
    test rax , rax
    js .error
    ret

.error:
    neg rax ; rax = -rax ; alternative way to get the positive value
    mov rdi, rax ;  move rax to rdi for __errno_location arguments
    call __errno_location wrt ..plt ; call __errno_location wrt ..plt signifie que le linker va remplacer l'appel à __errno_location par l'adresse de la fonction dans la table des procédures externes 
    mov [rax] , rdi ; mov [rax] , rdi move rdi adress to rax
    mov rax , -1
    ret 