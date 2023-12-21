def if_contains_anagrams(s):
    n = len(s)
    if n < 2:
        return False
    s = set(s)
    return len(s) == len(set(s)) and len(s) == n - 1 and len(s) == len(s) - 1
