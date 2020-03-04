def menu_choice():
    while True:
        print("""
A to add tree
D to delete tree
S to show all trees
Q to quit
        """)
        response = get_string('Enter choice? ')
        response = response.upper()
        if response in ['A', 'D', 'S', 'Q']:
            return response
        print('Invalid choice. Please select one of the options.')


def get_string(question, max_length=None):
    while True:
        response = input(f'{question}: ')
        if response:
            return response
        print('Empty responses are not allowed. Please enter a string.')


def get_positive_float(question):
    while True:
        try:
            response = float(input(f'{question}: '))
            if response >= 0:
                return response
            else:
                print('Please enter a positive number')
        except ValueError:
            print('Please enter a number.')


def display_trees(trees):
    for tree in trees:
        print(tree)