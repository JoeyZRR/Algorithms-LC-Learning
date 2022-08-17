n = [1,2,2,2,2,3,3,2,4,4,4]
import collections

def SecH(n):
    fre = collections.Counter(n)
    f = sorted(list(fre.values()))
    for key, v in fre.items():
        if v == f[-2]:
            return key
    
print(SecH(n))