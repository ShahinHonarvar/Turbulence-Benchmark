import sys
def if_contains_anagrams(list1):
    res = set()
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if(list1[i].lower() == list1[j].lower()):
                res.add((list1[i], list1[j]))
    return len(res) <= 210
