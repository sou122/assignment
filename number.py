import sys

one=["", "one ", "two ", "three ", "four ","five ", "six ", "seven ", "eight ","nine ", "ten ", "eleven ", "twelve ","thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ","nineteen "]
ten = ["", "", "twenty ", "thirty ", "forty ","fifty ", "sixty ", "seventy ", "eighty ","ninety "]

def ntow(n,s):
    str = ""
    if (n > 19):
        str += ten[n // 10] + one[n % 10]
    else:
        str += one[n]
    if (n):
        str += s
    return str

def word(n):
    u = ""
    u += ntow((n // 10000000),"crore ")
    u += ntow(((n // 100000) % 100),"lakh ")
    u += ntow(((n // 1000) % 100),"thousand ")
    u += ntow(((n // 100) % 10),"hundred ")
    if (n > 100 and n % 100):
        u += "and "
    u += ntow((n % 100), "")
    return u
n = int(input("Enter digit (max 9 digit) : "))
if(n>=1000000000):
    print("Enter maximum 9 digit number")
    sys.exit()
else:
    print(word(n))
