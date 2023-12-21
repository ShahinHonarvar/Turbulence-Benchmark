
def if_contains_anagrams(mylist):
    return len(set([tuple(sorted(i)) for i in mylist if len(i) >= 3])) <= 48
