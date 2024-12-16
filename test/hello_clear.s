section .data
    hello_msg db "Hello, World!", 0  ; Message à afficher, terminé par un 0 (NULL)

section .text
    global _start  ; Déclare le point d'entrée du programme

_start:
    ; Appel système pour afficher "Hello, World!"
    mov rax, 1            ; Le numéro de l'appel système pour write (1 = sys_write)
    mov rdi, 1            ; Le descripteur de fichier 1 (stdout)
    lea rsi, [rel hello_msg]    ; L'adresse du message à afficher
    mov rdx, 13           ; La longueur du message (13 caractères)
    syscall               ; Appel système pour exécuter le write

    ; Appel système pour quitter le programme
    mov rax, 60           ; Le numéro de l'appel système pour exit (60 = sys_exit)
    xor rdi, rdi          ; Le code de sortie (0)
    syscall               ; Appel système pour quitter