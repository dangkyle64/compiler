
class lexical:
    
    def __init__ (self):
        self.value = 0

    #lexer function
    def lexer(self, input):
        keyword = {
            "while" : "keyword",
            "class" : "keyword"
            
        }
        #setting state at beginning
        state = 'current_state'

        #test = 'hello_world' 
        test = input 

        #convert to string if integer input is found
        test = str(test)

        #split the inputs into characters to be put into the lexer function
        for index in range (len(test)):

            #inputs being put in one by one into input char
            input_char = test[index]

            #testing for starting underscore that makes identifiers invalid
            if (test[0] == '_'):
                print (f'invalid token: ERROR, Lexume: {test}')
                return 0
            
            #get the specific type to compare with the transition table
            input_type = self.get_input_type(input_char)

            #find where the next state is after transition 
            next_state_location = self.next_state(state, input_char)
            state = next_state_location
            #print (f'aaa: {state}')
            #print ("next_state:", next_state_location)

            #print (test[index])

        #when finishing moving through input and states, print results
            
        if ('identifier_continue' in state and test in keyword):
            print (f'Accepted State -> Token: keyword, Lexume {test}')
            
        elif ('identifier_continue' in state or 'identifier_start' in state):
            print (f'Accepted State -> Token: identifier, Lexume: {test}')

        elif ('integer_continue' in state):
            print (f'Accepted State -> Token: integer, Lexume: {test}')     

        elif ('operator' in state):
            print (f'Accepted State -> Token: operator, Lexume: {test}')

        elif ('separator' in state):

            print (f'Accepted State -> Token: separator, Lexume: {test}')

        elif ('real_continue' in state):
            print (f'Accepted State -> Token: real, Lexume: {test}')

        else:
            print (f'Token: ERROR, Lexume: {test}')

        return 0

    #find next transition state using dictionary and in puts
    def next_state(self, current_state, input_char):

        #create dictionary to define the different transitions 
        transitions = {
            "current_state": {
                "alpha": "identifier_start",
                "digit": "integer_start",
                "operator": "operator_start",
                "separator": "separator_start",
                "other": "invalid_input"
            },

            "identifier_start": {
                "alpha": "identifier_continue",
                "other": "invalid_input"
            },

            "identifier_continue": {
                "alpha": "identifier_continue",
                "digit": "identifier_continue",
                "other": "invalid_input"
            },

            "integer_start": {
                "digit": "integer_continue",
                "other": "invalid_input"
            },

            "integer_continue": {
                "digit": "integer_continue",
                "decimal": "real_start",
                "other": "invalid_input"
            },

            "operator_start":  {
                "all": "operator"
            },

            "separator_start": {
                "all": "separator"
            },

            "real_start": {
                "digit": "real_continue",
                "other": "invalid_input"
            },

            "real_continue": {
                "digit" : "real_continue",
                ".": "invalid_input",
                "other" : "invalid_input"

            },

            "invalid_input": {
                "all": "invalid"
            }

        }

        input_type = self.get_input_type(input_char)
        #print ("Input type:", input_type)

        next_state_dictionary = transitions.get (current_state, {})
        #print ("Next state dictionary", next_state_dictionary)

        next_state = next_state_dictionary.get(input_type, "invalid")
        #print ("Next state:", next_state)

        return next_state

    #find the type of input to get proper comparisons in dictionary
    def get_input_type(self, input_char):

        special_char_dict = {
            "=": "operator",
            "+": "operator",
            "-": "operator",
            "*": "operator",
            "/": "operator",
            "<": "operator",
            ">": "operator",
            ";": "separator",
            "(": "separator",
            ")": "separator",
            '"': "separator",
            ":": "separator"
        }

        if input_char.isalpha() or input_char == '_':
            return "alpha"
        
        if input_char.isdigit():
            return "digit"
        
        if input_char in special_char_dict:
            #print(f'aaaaaaa  {special_char_dict[input_char]}')
            return special_char_dict[input_char]
        
        if input_char == '.':
            return "decimal"
        
        else:
            return "other"
