CC := gcc

CFLAGS := -W -Wall -Wextra -Werror -O2

SRC	:= ./src/main.c

OBJ := $(SRC:.c=.o)

NAME := mst

.PHONY: all $(NAME) run clean test test-performance

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(OBJ) -o $(NAME)

run: $(NAME)
	./$(NAME) input_mst.txt output_mst.txt

test: $(NAME)
	python3 ./test/run_tests.py

test-performance: $(NAME)
	python3 ./test/test_performance.py

clean:
	$(RM) $(OBJ) $(NAME) output_mst.txt
