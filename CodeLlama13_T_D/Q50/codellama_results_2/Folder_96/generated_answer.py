
def if_contains_anagrams(mylist):
    return len([s for s in mylist if len(set(s)) < 3]) >= 98
