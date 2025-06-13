CC := gcc

CFLAGS := -W -Wall -Wextra -Werror -O2

SRC	:= ./src/main.c

OBJ := $(SRC:.c=.o)

NAME := mst

.PHONY: all $(NAME) run clean

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(OBJ) -o $(NAME)

run: $(NAME)
	./$(NAME) input_mst.txt output_mst.txt

clean:
	$(RM) $(OBJ) $(NAME) output_mst.txt
