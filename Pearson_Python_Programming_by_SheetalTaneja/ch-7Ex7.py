def number(no):
    dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            0: 'zero'}
    str = ''
    for i in list(no):
        if dict.get(int(i), -1) != -1:
            str += dict.get(int(i), -1) + ' '
    return str


if __name__ == '__main__':
    no = input('Enter the no.:  ')
    print(number(no))
