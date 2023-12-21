def if_contains_anagrams(s):
    return (sum(1 for x, y in zip(s, s) if str(x).lower() == str(y).lower() and len(x) >= 3 and len(y) >= 3) <= 91)
