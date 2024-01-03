'''This is a module to store objects that I use regularly.'''


vertical_space = '\n' * 12
dash_line = '-' * 64

    
def caseless_input(prompt):
    """This function returns all-lowercase input."""
    reply = input(prompt)
    reply = reply.lower()
    return reply


def menu(options_dict):
    """This function prints a formatted list of options longer than one
    character from a dictionary, then takes the user's selection and
    passes it to run_selection()
    """
    print('\nThe following options are available:')
    for key in options_dict:
        if len(key) > 1:
            print('\t' + key.title())
    selection = caseless_input('\nEnter your selection: ')
    run_selection(selection, options_dict)


def run_selection(selection, options_dict):
    """This function compares a user's selection against a dictionary of
    options and runs the corresponding function, or else notifies the
    user that the selection was invalid.
    """
    selection_validated = False
    for key in options_dict:
        if selection == key:
            options_dict[key]()
            selection_validated = True
    if not selection_validated:
        print('Invalid selection.')