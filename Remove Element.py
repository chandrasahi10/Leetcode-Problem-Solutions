def remove_element(nums,target):
    while target in nums:
        nums.remove(target)
    return nums
nums = list(map(int, input().split()))
target = int(input())
print(remove_element(nums,target))
