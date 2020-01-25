def func0a(nRow):
    for i in range(1, nRow + 1):
        num = 1
        while num != i + 1:
            print(num, end=' ')
            num += 1
        print()


def func0c(nRow):
    for i in range(nRow, 0, -1):
        num = 1
        while num != i + 1:
            print(num, end=' ')
            num += 1
        print()


def func0b(nRow):
    nspace = nRow - 1
    for i in range(1, nRow + 1):
        print('  ' * nspace, end=' ')
        nspace -= 1
        for num in range(i - 1, 1, -1):
            print(num, end=' ')
        for num in range(1, i):
            print(num, end=' ')
        print()


def func0d(nRow):
    for i in range(1, nRow + 1):
        num = 1
        while num != i + 1:
            print(i, end=' ')
            num += 1
        print()


def func0e(nRow):
    for i in range(1, nRow + 1):
        num = i
        nspace = i - 1
        print('  ' * nspace, end='')
        while num != nRow + 1:
            print(num, '', end='')
            num += 1
        print()


def func0f(nRow):
    for i in range(1, nRow + 1):
        if i == 1 or i == nRow:
            print('* ' * nRow)
        else:
            num = 1
            while num != nRow + 1:
                if num == 1 or num == nRow:
                    print('* ', end='')
                else:
                    print('  ',end='')
                num += 1
            print()


def func0g(nRow):
    for i in range(1,nRow+1):
        print('* '*nRow)


def func0h(nRow):
    nspace=nRow-1
    for i in range(1,nRow+1):
        print('  '*nspace,end='')
        for num in range(i - 1, 1, -1):
            print('*', end=' ')
        for num in range(1, i):
            print('*', end=' ')
        print()
        nspace-=1


def func0i(nRow):
    nspace=0
    for i in range(nRow,0,-1):
        if i==nRow:
            print("*   " * nRow)
        elif i==1:
            print('  '*nspace+'* ')
        else:
            print('  '*nspace+'*'+'    '*(i-1)+'* ')
        nspace+=1


def func0l(nRow):
    nspace = nRow-1
    for i in range(1,nRow):
        print('  ' * nspace, '* ' * (2 * i - 1))
        nspace -= 1
    nspace=0
    for i in range(nRow,0,-1):
        print('  '*nspace,'* '*(2*i-1))
        nspace+=1


def func0k(nRow):
    num=1
    nspace=nRow-1
    for i in range(1,nRow+1):
        if i==1:
            print('  '*nspace+'* ')
        else:
            print('  '*nspace+'* '+'  '*num+'* ')
            num+=2
        nspace-=1
    nspace=1
    num-=4
    for i  in range(nRow-1,0,-1):
        if i==1:
            print('  '*nspace+'* ')
        else:
            print('  '*nspace+'* '+'  '*num+'* ')
            num-=2
        nspace+=1


if __name__ == '__main__':
    func0i(5)
