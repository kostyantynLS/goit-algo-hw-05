'''
Четверте завдання

Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з 
клавіатури, та буде відповідати відповідно до введеної команди.

☝ Бот помічник повинен стати для нас прототипом застосунку-асистента, який ми 
озробимо в наступних домашніх завданнях. Застосунок-асистент в першому наближенні
 повинен вміти працювати з книгою контактів та календарем.
'''
import datetime
from functools import wraps

def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_contact":
                return(f'{func.__name__} : use ADD [name] [phone]')
            if func.__name__ == "change_contact":
                return(f'{func.__name__} : use CHANGE [name] [phone]')
            elif func.__name__ == "change_contact":
                return(f'{func.__name__} : use CHANGE [name] [phone]')
            else:
                return(f'{func.__name__} : Enter the argument for the command')
        except TypeError:
            if func.__name__ == "get_phone":
                return(f'{func.__name__} : use PHONE [name]')
            else:
                return(f'{func.__name__} : Enter the argument for the command')
        except KeyError:
            return(f'{func.__name__} : Enter the argument for the command')
        except Exception as e:
            return(f'{func.__name__} : Enter the argument for the command')
    return wrapper

@input_error
def say_hello():
    return "How can I help you?"

@input_error
def parse_input(cmd_line:str):
    info = cmd_line.split(" ")
    info[0] = info[0].strip(" ").lower()
    return info

@input_error
def add_contact(args, cont) -> str:
    name, phone = args
    cont[name] = phone
    return "contact added"

@input_error
def change_contact(args, cont) -> str:
    name, phone = args
    if name in cont:
        cont[name] = phone
        return "contact updated"
    else:
        return "contact not found"

@input_error
def del_contact(args, cont) -> str:
    name = args[0]
    if name in cont:
        del cont[name]
        return "contact deleted"
    else:
        return "contact not found"

@input_error
def print_contact(cont):
    items = list()
    if len(cont)>0:
        for names, phones in cont.items():
            items.append(f'{names},{phones}')
    return items

@input_error
def get_phone(name, cont):
    s = cont[name]
    return(s)

def curr_date():
    dt = datetime.datetime.now()
    return dt.strftime("%Y-%m-%d")

def curr_time():
    dt = datetime.datetime.now()
    return dt.strftime("%H:%M:%S")

@input_error
def main():

    contacts = dict()

    CLI_header = '****************************************\n'\
                 '**         Command line assistant     **\n'\
                 '****************************************\n'

    print(CLI_header)
    print(say_hello())
    while True:
        text = input('Type here your command: ')
        cmds = parse_input(text)
        if cmds[0]=='help':
            print(CLI_header)
            print('type "list" to see all commands')
        elif cmds[0]=='list':
            print(  'bye, exit, close  - exit from assistant\n'\
                    'help              - get help\n'\
                    'add name phone    - add phone to contact list\n'\
                    'del name          - delete contact from list\n'\
                    'change name phone - update phone number for name\n'\
                    'all               - print all contact book\n'\
                    'phone name        - get phone number for name\n'\
                    'date              - get current date\n'\
                    'time              - get current time\n'\
                    'list              - get commands list')
        elif cmds[0] in ['bye','exit','close']:
            print('good bye')
            break
        elif cmds[0]=='hello':
            print(say_hello())
        elif cmds[0]=='add':
            print(add_contact(cmds[1:], contacts))
        elif cmds[0]=='del':
            print(del_contact(cmds[1:], contacts))
        elif cmds[0]=='change':
            print(change_contact(cmds[1:], contacts))
        elif cmds[0]=='phone':
            print(get_phone(cmds[1:], contacts))
        elif cmds[0]=='all':
            us_list = print_contact(contacts)
            for i in us_list:
                print(' item: ', i)
        elif cmds[0]=='date':
            print(curr_date())
        elif cmds[0]=='time':
            print(curr_time())
        else:
            print(f'I don\'t understand {cmds[0]}')

if __name__ == "__main__":
    main()
