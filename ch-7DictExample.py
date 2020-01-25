def buildInDict(dict):
    inv = {}
    for key, value in dict.items():
        if value in inv:
            inv[value].append(key)
        else:
            inv[value] = [key]
    inv = {x: inv[x] for x in inv if len(inv[x] )> 1}
    return inv


def main():
    # wordmeaning = eval(input('enter word-meaning dict:'))
    wordmeaning = {'dubious': 'doubtful', 'hilarious': 'amusing', 'suspicious': 'doubtful', 'comical': 'amusing',
                   'hello': 'hi'}
    meaningword = buildInDict(wordmeaning)
    print('Inverted Dictionary:\n', meaningword)


if __name__ == '__main__':
    main()
