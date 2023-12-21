
def if_contains_anagrams(mylist):
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):
            if "".join(sorted(mylist[i].lower())) == "".join(sorted(mylist[j].lower())):
                continue
            else:
                return False
    return True
