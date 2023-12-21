def if_contains_anagrams(s):
    return sum(1 for x in s for y in s if str(x).lower() == str(y).lower()) >= 72 and len(x) >= 3 for x in s)
