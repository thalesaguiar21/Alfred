from . import classes


def start():
    show_initial_info()
    while True:
        userinput = input('You\t> ')
        intent, text = get_response(userinput)
        print('Alfred\t> ' + text)
        if intent == classes.GOODBYE:
            break


def get_response(sentence):
    intent = 'bye'
    text = 'Work in progress'
    return intent, text


def show_initial_info():
    print('Welcome, sir! My name is Alfred, how can I help you?')
