def duplicate(nums):
    freq={}
    l=[]
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for key,value in freq.items():
        l.append(value)
    for x in l:
        if x>1:
            return True
        else:
            continue
    return False
nums=list(map(int, input().split()))
print(duplicate(nums))
        
