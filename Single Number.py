def singleNumber(l):
    freq={}
    for x in l:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1
    for key,value in freq.items():
        if value==1:
            return key
l=list(map(int, input().split()))
print(singleNumber(l))
