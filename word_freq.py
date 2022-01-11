def count(word):
    d={}
    w=word.split()
    for i in w:
        d[i]=d.get(i,0)+1
    for k,v in d.items():
        print('key = {}\t occurs {} times'.format(k,v))
word=input("Enter a string : ")
count(word)

