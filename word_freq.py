'''def count(word):
    d={}
    w=word.split()
    for i in w:
        d[i]=d.get(i,0)+1
    for k,v in d.items():
        print('key = {}\t occurs {} times'.format(k,v))
word=input("Enter a string : ")
count(word)'''

import sys

print("1.Insert\n2.Delete\n3.Search\n4.Quit\n5.Display\n")
d={}
while(1):
    ch=int(input("Enter your choice : "))
    f = 0
    if(ch==1):
        d={}
        print("How many elements : ")
        n=int(input())
        for i in range(n):
            print("Enter book id",end=" ")
            k=input()
            print("Enter book name",end=" ")
            v=input()
            '''print("Enter author", end=" ")
            s = input()
            print("Enter book cost", end=" ")
            t = input()'''
            d.update({k:v})
        print(d)
    '''if(ch==2):
        id=int(input("enter id to delete : "))
        p=d.pop(k)
        print(d)'''
    if(ch==3):
        s=int(input("Enter the ID to search : "))
        for s in d.items():
            if s in d.items():
                f=1
        if(f==1):
            print(d)
        else:
            print("not present")
    if(ch==4):
        sys.exit()
    if(ch==5):
        print(d)
    if(ch==2):
        '''d = {1: 'b1', 2: 'b2', 3: 'b3', 4: 'b4', 5: 'b5'}'''
        id = int(input("enter id to delete : "))
        dele = [i for i in d if i in id]
        for i in dele: del d[i]
        print(d)