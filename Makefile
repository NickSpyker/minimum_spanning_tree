CC = gcc

CFLAGS = -W -O2

all: mst

mst: mst.c
	$(CC) $(CFLAGS) mst.c -o mst

run: mst
	./mst input_mst.txt output_mst.txt

clean:
	$(RM) mst output_mst.txt
