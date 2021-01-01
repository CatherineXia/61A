
def indent(str, number_of_spaces):
    print(" " * number_of_spaces + str)


def center(str, screen_width):
    indent_spaces = (int) (screen_width / 2)
    indent(str, indent_spaces)
    return indent_spaces


def read_n_center_text():
    str = input("Type Text String: ")
    screen_width = int(input("Enter Screen Width: "))
    indent_spaces = center(str, screen_width)
    print("Indented by", indent_spaces, "white spaces")

def print_moar(stuff):
    i = 0
    while stuff and i < 2:
        stuff = print(stuff, print('colin'))
        i += 1
    return stuff


def square(x):
    return x * x

def argentina(n):
    print(n)
    if n > 0:
        return lambda k: k(n+1)
    else:
        return 1 / n


def yak(zebra):
    return 20 // zebra
def llama(alpaca):
    zebra = 0
    def yak(zebra):
        return alpaca(zebra)
    return yak


if __name__ == '__main__':
    indent("Hello", 0)
    indent("Hi", 5)
    center("my lucky number is 888", 80)
    read_n_center_text()
