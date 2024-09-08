from colorama import Fore
import sys
from pathlib import Path


def main():
    global num
    num = 0
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        try:
            dir_tree(path)

        except (OSError, FileNotFoundError):
            print("Wrong path, Please try again")

    else:
        print('No path is entered')


def dir_tree(path):
    global num

    for element in path.iterdir():
        if element.is_dir():
            print(num*' ', Fore.GREEN + element.name)
            num += 3
            dir_tree(element)
            num -= 3
        else:
            print(num*' ', Fore.BLUE + element.name)


if __name__ == "__main__":
    main()
