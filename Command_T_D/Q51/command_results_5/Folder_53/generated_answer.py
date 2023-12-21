def if_contains_anagrams(list):
    return len(list) <= 8 and sum(1 for s in list if s in s.lower()) <= 8
