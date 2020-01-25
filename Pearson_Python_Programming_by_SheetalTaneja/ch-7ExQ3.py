def frequencyCounter():
    #lst = list(input('Enter sentence'))
    fdict = {}
    for i in list(input('Enter sentence: ')):
        if fdict.get(i, -1) == -1:
            fdict[i] = 1
        else:
            fdict[i] += 1
    print(fdict)


if __name__ == '__main__':
    frequencyCounter()
