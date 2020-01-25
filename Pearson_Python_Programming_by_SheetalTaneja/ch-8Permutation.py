def per(l1,l2=[],k=0,pos=0):
    l2.insert(pos,l1[k])    #To insert element at l1[k] at current pos
    if len(l2)==len(l1):
        print(l2)   #if  permutation is generated
    else:
        per(l1,l2,k+1,0)    #To insert element l1[k+1]
    l2.remove(l1[k])    #To remove other permutations, remove element l1[k] from cur pos
    if pos<k:
        per(l1,l2,k,pos+1)  #put element at next available pos


if __name__ == '__main__':
    l1= eval(input('Enter the list: '))
    per(l1)