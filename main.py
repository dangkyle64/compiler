from lexer import lexical
from lexer import Token

def main():

    inputs = []
    lexical_analyzer = lexical()

    #read file and put into an array without newlines
    with open ('input_scode.txt', 'r') as file:
        for line in file:
            inputs_array = line.split(" ")
            inputs.extend(inputs_array)
        #file_data = [line.strip() for line in file.readlines()]
        #print(file_data)

    #loop through all testcases in lexical analyzer
    for input in inputs:
        token_output = lexical_analyzer.lexer(input)
        print (f'{token_output.type}, {token_output.lexume}')

    return 0

if __name__ == '__main__':
    main()