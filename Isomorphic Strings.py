def isIsomorphic(s,t):
    d = {}
    for x in range(len(s)):
        char1, char2 = s[x], t[x]
        if char1 not in d:
            if char2 in d.values():
                return False
            d[char1] = char2
        elif d[char1] != char2:
            return False
    return True

s=input()
t=input()
print(isIsomorphic(s,t))
