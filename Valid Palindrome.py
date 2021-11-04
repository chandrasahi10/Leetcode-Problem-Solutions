def isPalindrome(s):
    str1=""
    for x in s:
        if (x.isalpha()==True or x.isdigit()==True):
            str1=str1+x
    if(str1 == " "):
        return True
    else:
        str2 = str1.lower()
        if(str2==str2[::-1]):
            return True
        return False
s=input()
print(isPalindrome(s))
        
            
