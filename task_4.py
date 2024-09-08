def parse_input(user_input : str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def perform_command(command, contacts, args ) :
    if command == 'add' :
        return add_command(contacts, args)
    elif command == 'change' :
        return change_command(contacts, args)
    elif command == 'phone' :
        return phone_command(contacts, args)
    elif command == 'all' :
        return all_command(contacts)
    else :
        return help_command()


def add_command(contacts, args):
    if args[0].capitalize() not in contacts.keys():
        contacts[args[0].capitalize()] = args[1]
        return 'Contact added' 
    else :
        return 'Contact already exists'


def change_command(contacts, args):
    if args[0].capitalize() in contacts.keys():
        contacts[args[0].capitalize()] = args[1]
        return 'Contact changed'
    else :
        return 'Contact does not exist'
    


def phone_command(contacts, args):
    if args[0].capitalize() in contacts.keys():
        return f'Phone number of {args[0].capitalize()} is {contacts[args[0].capitalize()]}'
    else :
        return 'Contact does not exist'


def all_command(contacts):
    return contacts


def help_command():
    return '''List of available commands :
"add username phone"; "change username phone"; "phone username"; "all"; "help"; "close" or "exit" '''
        


def main():
    contacts = {}
    commands = ['add', 'change', 'phone', 'all', 'help']
    print('Good Day, User, How can i help you ? To see a list of comands use command "help".\n')
    while True :
        user_input = input("Please write command\n")
        command , *args = parse_input(user_input) 
        
        if command in ['close', 'exit'] :
            print('Goodbye, User!')
            break
        elif command == "hello" :
            print("Hello, User! How can I help you ?")
        elif command in commands :
            try :
                print(perform_command(command, contacts, args))
            except IndexError :
                print('Some information is missing. Please try again')
        else :
            print("Command is not identified")
        
         
if __name__ == '__main__' :
    main()
         