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