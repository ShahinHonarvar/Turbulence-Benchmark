
def if_contains_anagrams(mylist):
    pairs = 0
    for i in range(len(mylist)):
        s1 = mylist[i].lower()
        for j in range(i+1, len(mylist)):
            s2 = mylist[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    pairs += 1
                    if pairs >= 44:
                        return True
    return False
