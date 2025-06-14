CC := gcc

CFLAGS := -W -Wall -Wextra -Werror -O2

SRC	:= ./src/main.c

OBJ := $(SRC:.c=.o)

NAME := mst

.PHONY: all $(NAME) run clean test

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(OBJ) -o $(NAME)

run: $(NAME)
	./$(NAME) input_mst.txt output_mst.txt

test: $(NAME)
	python3 ./test/functional_tests.py

clean:
	$(RM) $(OBJ) $(NAME) output_mst.txt
	$(RM) -r test_outputs/
