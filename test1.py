import collections
s = "aababbb"

def largestVariance(s):

    variance = 0
    if len(set(s)) == len(s):
        return 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if len(set(s[i:j])) == 1:
                continue
            dct = collections.Counter(s[i:j])
            value = dct.values()
            lst = list(value)
            cur = max(lst) - min(lst)
            if cur > variance:
                variance = cur
    return variance

print(largestVariance(s))