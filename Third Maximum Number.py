def thirdMax(nums):
    f={}
    l=[]
    for x in nums:
        if x in f:
            f[x]+=1
        else:
            f[x]=1
    for key,value in f.items():
        l.append(key)
    if (len(l)>=3):
        l.sort(reverse=True)
        return(l[2])
    else:
        return(max(l))

nums=list(map(int, input().split()))
print(thirdMax(nums))
