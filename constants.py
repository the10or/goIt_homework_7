from colorama import Fore, Back, Style

B = Fore.BLUE
G = Fore.GREEN
Y = Fore.YELLOW
R = Fore.RESET

INVITE_MESSAGE = "Please enter your command here or type 'help' to see the list of commands: >>> "
NO_RECORD_ERROR_MESSAGE = "Sorry, there's no such record, enter another name or check your spelling"
QUIT_COMMANDS = ("good bye", "close", "exit")
WRONG_NUMBER_OF_PARAMETERS_ERROR_MESSAGE = "Wrong number of parameters, please check your input"
EMPTY_MESSAGE = "No records in this address book"
HELLO_MESSAGE = "How can I help you?"
INVALID_COMMAND_ERROR_MESSAGE = "Invalid command, please check your input"
BYE_MESSAGE = "Good bye!"
COMMANDS_LIST = (f'''{G}
Available commands:
    
    {B}add{R} [name] [phone] {G}- Adds a new contact to the address book with the given name and phone number.
    {B}change{R} [name] [old phone number] [new phone number] {G}- Changes the phone number of the contact with the given name.
    {B}exit,
    close,
    good bye {G}- Exits the program.
    {B}find {R}[part of the name]/[part of the phone] {G}- Finds the contact with the given part of the name or phone number.
    {B}hello {G}- Greeting message.
    {B}phone {R}[name] {G}- Shows the phone number of the contact with the given name.
    {B}show all {G}- Shows all the contacts in the address book.
    {B}show all" {R}[num] {G}- Shows the first num contacts in the address book.{R}
     ''')
