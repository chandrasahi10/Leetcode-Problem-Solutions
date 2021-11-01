def two_sumII(nums,target):
    compliment={}
    for i in range(len(nums)):
        if nums[i] in compliment:
            return(compliment[nums[i]]+1,i+1)
        else:
            compliment[target-nums[i]]=i
nums=list(map(int, input().split()))
target=int(input())
print(two_sumII(nums,target))
