
def if_contains_anagrams(mylist):
    return len([x for x in mylist if len(x) >= 3 and sorted(x.lower()) in map(sorted, mylist[:len(mylist)-1])]) > 54
