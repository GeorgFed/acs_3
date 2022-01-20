from container import *
import sys


def main():
    container = Container()
    try:
        if len(sys.argv) == 5 and sys.argv[1] == '-n' and sys.argv[2].isdecimal():
            generate_random(container, amount=int(sys.argv[2]))
        elif len(sys.argv) == 5 and sys.argv[1] == '-f':
            file_commands(container, filepath=sys.argv[2])
        else:
            print('Something went wrong, please try again.')
        container.write(sys.argv[3])
        container.sort()
        container.write(sys.argv[4])
        # Test Generator Function:
        # container.test_write(sys.argv[3])
    except Exception as error:
        print(f'Something went wrong, error: {error}')

def file_commands(container, filepath):
    container.read(filepath)


def generate_random(container, amount):
    container.generate(amount=amount)


if __name__ == '__main__':
    main()
