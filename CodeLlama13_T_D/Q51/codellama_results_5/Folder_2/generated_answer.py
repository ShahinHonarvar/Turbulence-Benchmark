
def if_contains_anagrams(mylist):
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):
            if sorted(mylist[i].lower()) == sorted(mylist[j].lower()):
                return True
    return False
