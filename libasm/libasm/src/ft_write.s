;C function prototype
; ssize_t write(int fd, const void *buf, size_t count);
;
; DESCRIPTION
; write() writes up to count bytes from the buffer starting at buf to
; the file referred to by the file descriptor fd.
;
; The number of bytes written may be less than count if, for example,
; there is insufficient space on the underlying physical medium, or
; the RLIMIT_FSIZE resource limit is encountered (see setrlimit(2)),
; or the call was interrupted by a signal handler after having writ‐
; ten less than count bytes. (See also pipe(7).)
;
; For a seekable file (i.e., one to which lseek(2) may be applied,
; for example, a regular file) writing takes place at the file off‐
; set, and the file offset is incremented by the number of bytes
; actually written. If the file was open(2)ed with O_APPEND, the file
; offset is first set to the end of the file before writing. The ad‐
; justment of the file offset and the write operation are performed
; as an atomic step.
;
; POSIX requires that a read(2) that can be proved to occur after
; a write() has returned will return the new data. Note that not all
; filesystems are POSIX conforming.
;
; According to POSIX.1, if count is greater than SSIZE_MAX, the re‐
; sult is implementation-defined; see NOTES for the upper limit on
; Linux.
;
; RETURN VALUE
; On success, the number of bytes written is returned. On error, -1
; is returned, and errno is set to indicate the cause of the error.
;
; Note that a successful write() may transfer fewer than count bytes.
; Such partial writes can occur for various reasons; for example, be‐
; cause there was insufficient space on the disk device to write all
; of the requested bytes, or because a blocked write() to a socket,
; pipe, or similar was interrupted by a signal handler after it had
; transferred some, but before it had transferred all of the requested
; bytes. In the event of a partial write, the caller can make another
; write() call to transfer the remaining bytes. The subsequent call
; will either transfer further bytes or may result in an error (e.g.,
; if the disk is now full).
;
; If count is zero and fd refers to a regular file, then write() may
; return a failure status if one of the errors below is detected. If
; no errors are detected, or error detection is not performed, 0 will
; be returned without causing any other effect. If count is zero and
; fd refers to a file other than a regular file, the results are not
; specified.

; ssize_t write(int fd, const void *buf, size_t count);

;Assembly function
;Arguments:
;   -rdi = file descriptor
;   -rsi = pointer to buffer
;   -rdx = number of bytes to write
;   -rax = number of bytes written


section .text
global ft_write
extern __errno_location ; pour trouver l'adresse de la fonction dans la table des procédures externes il faut faire la commande suivante : nm -D /usr/lib/x86_64-linux-gnu/libc.so.6 | grep __errno_location
;                                                                                                                                            nm -D (pour afficher les symboles dynamiques) path_to_lib (fichier de la libc) | grep fonction name

ft_write:
    mov rax, 1
    syscall
    test rax , rax
    js .error
    ret

.error:
    neg rax ; rax = -rax ; alternative way to get the positive value
    mov rdi, rax ; 
    call __errno_location wrt ..plt
    mov [rax] , rdi ;
    mov rax , -1
    ret





