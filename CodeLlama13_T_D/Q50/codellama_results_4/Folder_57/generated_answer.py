
def if_contains_anagrams(mylist):
    pairs = 0
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):
            if set(mylist[i].lower()) == set(mylist[j].lower()):
                pairs += 1
                if pairs >= 50:
                    return True
    return False
