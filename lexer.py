#create dictionary to define the different transitions 
transitions = {
    "current_state": {
        "alpha": "identifier_start",
        "digit": "integer_start",
        "other": "invalid_input"
    },

    "identifier_start": {
        "alpha": "identifier_continue",
        "alnum": "identifier_continue",
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
        "other": "invalid_input"
    },

    "invalid_input": {
        "all": "invalid"
    }

}

#lexer function
def lexer():

    #setting state at beginning
    state = 'current_state'

    #inputs would go here (future file inputs to test inputs would also go here)
    #potentially make a separate function that would return into the lexer specifically

    #test cases
    #test = 'hello' #should complete, print alphas
    #test = '_123' #should fail, cannot have underscore to start
    test = 123 #should complete, print integers
    #test = 'hello123'
    #test = 'hello_world' #need to check this

    #convert to string if integer input is found
    test = str(test)

    #split the inputs into characters to be put into the lexer function
    for index in range (len(test)):

        #inputs being put in one by one into input char
        input_char = test[index]

        #get the specific type to compare with the transition table
        input_type = get_input_type(input_char)

        #find where the next state is after transition 
        next_state_location = next_state(state, input_char)
        state = next_state_location
        #print (f'aaa: {state}')
        print ("next_state:", next_state_location)

        #print (test[index])

    if ('identifier_continue' in state):
        print (f'Token: identifier, Lexume: {test}')

    elif ('integer_continue' in state):
        print (f'Token: integer, Lexume: {test}')     

    else:
        print ('invalid token')

    return 0

#find next transition state using dictionary and in puts
def next_state(current_state, input_char):
    input_type = get_input_type(input_char)
    print ("Input type:", input_type)

    next_state_dictionary = transitions.get (current_state, {})
    #print ("Next state dictionary", next_state_dictionary)

    next_state = next_state_dictionary.get(input_type, "invalid")
    #print ("Next state:", next_state)

    return next_state

#find the type of input to get proper comparisons in dictionary
def get_input_type(input_char):
    if input_char.isalpha():
        return "alpha"
    
    if input_char.isdigit():
        return "digit"
    
    if input_char.isalnum():
        return "alnum"
    
    else:
        return "other"

lexer()