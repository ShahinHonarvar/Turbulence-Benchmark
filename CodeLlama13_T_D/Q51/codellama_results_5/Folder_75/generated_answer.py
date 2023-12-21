
def if_contains_anagrams(lst):
    return len([i for i in lst if ''.join(sorted(i)) in lst]) <= 55
