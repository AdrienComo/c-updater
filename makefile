B = bin
O = obj
S = src
FLAGS = -c -Wall
PYTHON_FLAGS = -I/usr/include/python3.8 -lpython3.8

all: $(O) $(B) $(B)/main


$(B)/main:  
	g++ $(S)/main.cpp $(PYTHON_FLAGS) -o $(B)/main && clear
	
$(O):
	mkdir $(O)

$(B):
	mkdir $(B)

clean: $(O) $(B)
	rm -rf $(O)
	rm -rf $(B)
