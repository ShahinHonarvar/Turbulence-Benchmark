
def palindromes_of_specific_lengths(s):
    import re
    from collections import defaultdict

    s = re.sub("[^a-zA-Z]", "", s[155:284]).lower()
    n = len(s)
    p = defaultdict(set)

    for i in range(n):
        for j in range(1,n-i+1):
            substr = s[i:i+j]
            if substr == substr[::-1] and 104 <= len(substr) <= 120:
                p[len(substr)].add(substr)

    return set(val for sublist in p.values() for val in sublist) if p else set()
