from lexer import lexical

def main():

    lexical_analyzer = lexical()

    #read file and put into an array without newlines
    with open ('input_scode.txt', 'r') as file:
        file_data = [line.strip() for line in file.readlines()]
        #print(file_data)

    #loop through all testcases in lexical analyzer
    for input in file_data:
        lexical_analyzer.lexer(input)

    return 0

if __name__ == '__main__':
    main()