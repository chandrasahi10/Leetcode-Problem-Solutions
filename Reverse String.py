def reverseString(s):
    start=0
    end=len(s)-1
    while(start<end):
        s[start], s[end] = s[end], s[start]
        start = start+1
        end = end-1
    return s

s=list(map(str, input().split()))
print(reverseString(s))
        
