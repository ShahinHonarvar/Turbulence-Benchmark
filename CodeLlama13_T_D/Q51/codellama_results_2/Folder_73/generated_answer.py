
def if_contains_anagrams(list_of_strings):
    return len([s for s in list_of_strings if len(set(s)) == 3 and len({''.join(sorted(s)) for s in list_of_strings}) > 279]) <= 279
