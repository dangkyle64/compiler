'''
def lexer()
    returns token, token_value = instance of token (lexeme)

implement FSA for tokens
    identifier and integers, others can be written extra

write REs
draw FSA for above required tokens (identifier and integer)
    put this into document called FSA_mydesign.doc

print result into 2 columns, one for token and one for lexemes
    save result into output.txt

    ex.

    token       lexeme
    keyword     while
    separator   ()
    identifier  t
    real        22.00

readme should include documentation and how to setup program

resulting files should have input_scode.txt, design_file, program_file, output_file, readme_file

States:
    S: Inital State
    A: Accepting State 

Alphabet
    {'variable_name',_underscored_word, myFunction, MOD_NAME, cat123, __init__, digits}

Transitions
    From State start_state:
        On input [a-zA-Z_]: Transition to identifier_start
        On input digits: Transition to integer_start
        Otherwise: Transition to invalid_input

    From State identifier_start:
        On input [a-zA-Z0-9_]: Transition to identifier_continue
        Otherwise: Transition to invalid_input

    From State identifier_continue:
        On input [a-zA-Z0-9_]: Transition to identifier_continue
        When finished: Transition to accepted_state
        Otherwise: Transition to invalid_input

    From State integer_start:
        On input [0-9]: Transition to integer_continue
        Otherwise: Transition to invalid_input

    From State integer_continue:
        On input [0-9]: Transition to integer_continue
        When finished: Transition to accepted_state
        Otherwise: Transition to invalid_input

    From State invalid_input
        any input: Transition to invalid

    From State invalid
        any input: return ERROR_TOKEN

    From State accepted_state:
        Accepting State (include different accepting states for each token)

'''
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
        "alnum": "identifier_continue",
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
    state = current_state

    #inputs would go here (future file inputs to test inputs would also go here)
    #potentially make a separate function that would return into the lexer specifically

    #test cases
    #test = 'hello' #should complete, print alphas
    #test = '_123' #should fail, cannot have underscore to start
    test = 123 #should complete, print integers

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

    if ('identifier_continue' in state or 'integer_continue' in state):
        print ('complete')
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

#setting state at beginning
current_state = "current_state"

#inputs being put in one by one into input char
input_char = "52"

#get the specific type to compare with the transition table
#input_type = get_input_type(input_char)
#print ("Input type", input_type)

#find where the next state is after transition 
#next_state = next_state(current_state, input_char)
#print ("next_state:", next_state)
lexer()