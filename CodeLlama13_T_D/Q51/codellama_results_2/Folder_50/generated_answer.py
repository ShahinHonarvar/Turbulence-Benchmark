
def if_contains_anagrams(mylist):
    count = 0
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):
            if set(mylist[i].lower()) == set(mylist[j].lower()):
                count += 1
                if count > 47:
                    return False
    return True
