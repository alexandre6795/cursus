#executable
NAME = prg

#compilateur c
CC = gcc
CFLAGS = -Wall -Wextra -Werror -g -Ilibasm/lib

#compilateur assembleur
ASM = nasm
ASM_FLAGS = -f elf64 -g # -f format de sortie. = elf linux 64 bits -g pour debug

#ASSEMBLEUR
#lib
#src
LIB_DIR = libasm
LIB = $(LIB_DIR)/lib/libasm.a
LIB_SRC = $(LIB_DIR)/src
LIB_FILES = ft_strlen.s\
			ft_strcpy.s\
			ft_strcmp.s\
			ft_write.s\
			ft_read.s\
			ft_strdup.s
			
LIB_FILES := $(addprefix $(LIB_SRC)/, $(LIB_FILES))

#obj
LIB_OBJ_DIR = $(LIB_DIR)/obj
LIB_OBJ = $(LIB_FILES:$(LIB_SRC)/%.s=$(LIB_OBJ_DIR)/%.o)
#C
#source
SRC_DIR = src
SRC_FILES = main.c
SRC_FILES := $(addprefix $(SRC_DIR)/, $(SRC_FILES))
OBJ = $(SRC_FILES:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

#obj
OBJ_DIR = obj
OBJ_SRC = $(SRC_DIR):%.c=$(OBJ_DIR):%.o

#bonus
BONUS_DIR = bonus
BONUS_SRC = $(BONUS_DIR)/src
BONUS_OBJ_DIR = $(BONUS_DIR)/obj
BONUS_FILES =
BONUS_OBJ = $(BONUS_SRC):%.c=$(BONUS_OBJ_DIR):%.o

all: $(NAME)
#création de l'exécutable
$(NAME): $(LIB) $(OBJ)
	$(info LIB = $(LIB))
	$(CC) $(CFLAGS) -o $(NAME) $(OBJ) $(LIB)
#compilation des fichiers C
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@
#compilation des fichiers ASM
$(LIB_OBJ_DIR)/%.o: $(LIB_SRC)/%.s
	$(ASM) $(ASM_FLAGS) -o $@ $<
#création de la bibliothèque statique	
$(LIB): $(LIB_OBJ)
	ar rcs $(LIB) $(LIB_OBJ)

clean:
	rm -rf $(OBJ_DIR)/*.o
	rm -rf $(LIB_OBJ_DIR)/*.o

fclean: clean
	rm -rf $(NAME)
	rm -rf $(LIB)

re: fclean all



bonus_clean:
	rm -rf $(BONUS_OBJ)/*.o

bonus_re: bonus_clean bonus

.PHONY: all clean fclean re bonus bonus_fclean bonus_re
