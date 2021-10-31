def two_sums(nums,target):
    compliments={}
    for i in range(len(nums)):
        if nums[i] in compliments:
            return(i,compliments[nums[i]])
        else:
            compliments[target-nums[i]]=i
nums=list(map(int, input().split()))
target=int(input())
print(two_sums(nums,target))
