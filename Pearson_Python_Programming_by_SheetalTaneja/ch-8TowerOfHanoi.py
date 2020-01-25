def hanoi(n,source,spare,target):
    if n==1:
        print('Move a disk from',source,'to',target)
    elif n==0:
        return
    else:
        hanoi(n-1,source,target,spare)
        print('Move a disk from',source,'to',target)
        hanoi(n-1,spare,source,target)


if __name__ == '__main__':
    n = int(input('Enter the no. of discs: '))
    source = int(input('Enter source pole: '))
    spare= int(input('Enter of spare pole: '))
    target = int(input('Enter target pole: '))
    hanoi(n,source,spare,target)