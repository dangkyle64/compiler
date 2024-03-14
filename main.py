from lexer import lexical

def main():

    inputs = []
    lexical_analyzer = lexical()

    #read file and put into an array without newlines
    with open ('input_scode.txt', 'r') as file:
        for line in file:
            inputs_array = line.split(" ")
            inputs.append(inputs_array)
        #file_data = [line.strip() for line in file.readlines()]
        #print(file_data)

    #loop through all testcases in lexical analyzer
    for input in inputs_array:
        lexical_analyzer.lexer(input)

    return 0

if __name__ == '__main__':
    main()