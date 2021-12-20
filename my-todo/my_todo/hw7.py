import argparse
import sys
import json


    
def load_data() -> list:
    """
    Read json

    :return: list
    """
    with open('todo.json', 'r') as f:
        list_of_affairs= json.load(f)
    return list_of_affairs

def update_json(list_of_affairs: list) -> None:
    """
    Update json file

    :return: None
    """
    with open('todo.json', 'w') as f:
        json.dump(list_of_affairs, f, ensure_ascii=False, indent=4)
       
def add(title: str, descr: str) -> None:
    """
    Add affair in todo list

    :return: None
    """
    list_of_affairs = load_data()
    list_of_affairs.append({'title':title, 'description':descr})
    update_json(list_of_affairs)
    sys.stdout.write("Succesfully added!")
    sys.stdout.write('\n')
        
def show(num: int) -> None:
    """
    Show first num affairs

    :return: None
    """
    list_of_affairs = load_data()
    if num > len(list_of_affairs):
        sys.stdout.write('Number is bigger than amount of affairs')
    elif num < 1:
        sys.stdout.write('Number should be neutral')
    else:
        for i in range(num):
            sys.stdout.write(list_of_affairs[-i]['title'])
            sys.stdout.write('\n')
           
def done(num: int) -> None:
    """
    Delete the affair number num

    :return: None
    """
    list_of_affairs = load_data()
    if num > len(list_of_affairs):
        sys.stdout.write('Number is bigger than amount of affairs')
    elif num < 1:
        sys.stdout.write('Number should be neutral')
    else:
        list_of_affairs.remove(list_of_affairs[len(list_of_affairs)-num])
        update_json(list_of_affairs) 
        sys.stdout.write("Succesfully done!")
        sys.stdout.write('\n')
    
def find(text: str) -> None:
    """
    Find an affair by title or description

    :return: None
    """
    list_of_affairs = load_data()
    for affair in list_of_affairs:
        if text in affair['title'] or text in affair['description']:
            sys.stdout.write(affair['title'])
            sys.stdout.write('\n')

def main():
    """
    Do the script.

    :return: None
    """
    str1 = 'Use commands: add, show, done,find'
    str2 = 'title-description/number/string'
    parser = argparse.ArgumentParser()
    
    parser.add_argument('com', type=str, help=str1)
    parser.add_argument('text', nargs='*', help=str2)
    
    args = parser.parse_args()
    
    if args.com == 'add':
        add(args.text[0], args.text[1])
    if args.com == 'show':
        show(int(args.text[0]))
    if args.com == 'done':
        done(int(args.text[0]))
    if args.com == 'find':
        find(args.text[0])