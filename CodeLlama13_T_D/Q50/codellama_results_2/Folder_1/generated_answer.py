
def if_contains_anagrams(lst):
    return len([x for x in lst if len(set(x)) == 3 and x[::-1] in lst]) >= 96
