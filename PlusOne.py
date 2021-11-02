def PlusOne(digits):
    str1 = ""
    for x in digits:
        str1 = str1 + str(x)
    num1 = int(str1)
    num1 = num1+1
    number = [int(x) for x in str(num1)]
    return number

digits = list(map(int, input().split()))
print(PlusOne(digits))
    
