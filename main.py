from lexer import lexical
from lexer import Token

def main():

    inputs = []
    lexical_analyzer = lexical()

    #read file and put into an array without newlines
    with open ('input_scode.txt', 'r') as file:
        for line in file:
            inputs_array = line.split(' ')
            inputs.extend(inputs_array)
        #print(file_data)

    #loop through all testcases in lexical analyzer
    with open ('output.txt', 'w') as file:
        file.write(f'Tokens, Lexume\n')
        for input in inputs:
            token_output = lexical_analyzer.lexer(input)
            #print (f'{token_output.type}, {token_output.lexume}')
            file.write(f'{token_output.type}, {token_output.lexume}\n')

    return 0

if __name__ == '__main__':
    main()