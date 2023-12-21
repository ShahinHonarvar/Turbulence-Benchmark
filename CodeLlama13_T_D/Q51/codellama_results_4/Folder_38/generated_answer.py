
def if_contains_anagrams(lst):
    return len([s for s in lst if is_anagram(s)]) <= 416

def is_anagram(s):
    return sorted(list(set(s))) == ['a', 'b', 'c', 'd', 'e']
