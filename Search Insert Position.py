def SearchInsert(l,target):
    lower=0
    upper=len(l)-1

    while lower<=upper:
        mid = (lower+upper)//2

        if l[mid]==target:
            return mid
        elif l[mid]<target:
            lower=mid+1
        else:
            upper=mid-1
    return lower

l=list(map(int, input().split()))
target = int(input())
print(SearchInsert(l,target))
