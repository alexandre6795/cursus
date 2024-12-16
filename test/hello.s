; rtfm pour les syscall
; rax correspond a la valeur transmis pour le prochain syscall
; rdi correspond au premier argument
; rsi correspond au deuxieme argument
; rdx correspond au troisieme argument
; r10 correspond au quatrieme argument
; r8 correspond au cinquieme argument
; r9 correspond au sixieme argument
section .data   ; cree une section de donnees (reserve de la memoire)
; les diff types de donnees pouvant etre dufinies dans cette section sont:
; db (define byte) - octet (8bits)
; dw (define word) - mot
; dd (define doubleword) - double mot
; dq (define quadword) - quad mot
; dt (define ten bytes) - dix octets
; d'autres format plsu ou moins specifiques existent
    hello_msg db "Hello, World!", 0 ; met dans la reserve memoire representer par hello_msg un string et ajoute le caractere null a la fin

section .text ; section de donnees pour le programme ou la fonction
global _start ; le point d'entree du programme

; rappel syscall write(uint fd, const char * buf, size_t count)
; write(ou est ecrit le message, message , taille du message)
_start:
    mov rax, 1 ; cette ligne utilise mov pour mettre 1 dans le registre rax ce qui correspond a la syscall pour write
    mov rdi, 1 ; met 1 dans le registre rdi qui correspond au premier argument de la syscall write ici 1 correspond a stdout
    mov rsi , hello_msg ; met l'adresse de hello_msg dans le registre rsi qui correspond au deuxieme argument de la syscall write
    ;lea rsi, [hello_msg] marche aussi car lea permet de mettre l'adresse de hello_msg dans rsi
    mov rdx , 13 ; met 13 dans le registre rdx qui correspond au troisieme argument de la syscall write ici 13 correspond a la taille du message
    syscall ; appelle la syscall pour les arguments mis dans les registres
    ; pendant le syscall le kernel va prendre le controle et executer les instruction donnees dans les differents registres
    ; puis il va retourner le controle au programme a la ligne suivante
    mov rax , 60 ; met 60 dans le registre rax qui correspond a la syscall pour exit
    xor rdi , rdi ; met 0 dans le registre rdi qui correspond au premier argument de la syscall exit ici 0 correspond a un exit sans erreur
    ; xor est utilise pour mettre 0 dans le registre rdi car xor avec lui meme donne toujours 0 ( ou exclusif)
    ; cette methode est souvent utilisee pour mettre 0 dans un registre et est plus rapide que mov rdi, 0
    syscall ; appelle la syscall pour les arguments mis dans les registres