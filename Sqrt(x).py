def squareroot(x):
    if x==0 or x==1:
        return x
    else:
        l=0
        u=x
        while l<=u:
            mid = (l+u)//2
            midsq = mid*mid

            if midsq == x:
                return mid

            elif midsq < x:
                l = mid+1
                ans = mid

            else:
                u = mid-1
    return ans

x = int(input())
print(squareroot(x))

#used concept of binary search.
#Program for binary search also given in the same repository.
