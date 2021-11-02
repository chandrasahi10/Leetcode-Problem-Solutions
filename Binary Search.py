def binary_search(a,n):
    l=0
    u=len(a)-1

    while l<=u:
        mid = (u+l)//2

        if a[mid]==n:
            return mid
        elif mid<n:
            l=mid+1
        else:
            u=mid-1
    return False

a = list(map(int, input().split()))
n = int(input())
pos = binary_search(a,n)

if pos==False:
    print('Not Found')
else:
    print('Found at position :',pos+1)
