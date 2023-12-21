import collections
def if_contains_anagrams(texts):
    seen = set()
    for s in texts:
        for i in range(1, len(s)+1):
            for j in range(1, len(s[0:i])+1):
                if s[i-1:i+j] in seen and s[i-1:i+j] != s[0:i]:
                    seen.add(s[i-1:i+j])
                    break
            else:
                seen.add(s)
                break
    return len(seen) <= 279
