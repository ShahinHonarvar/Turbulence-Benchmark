def if_contains_anagrams(s):
    return (len(s) - len(set(s))) * 2 <= 59
