def isPowerOfTwo(n):
    if n==0:
        return False
    return n&(-n)==n
n=int(input())
print(isPowerOfTwo(n))

'''def isPowerOfTwo(n):
    if n==0:
        return False
    while n%2==0:
        n=n/2
    return n==1
n=int(input())
print(isPowerOfTwo(n))'''
    
