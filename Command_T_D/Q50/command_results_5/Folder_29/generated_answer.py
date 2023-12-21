import itertools
def if_contains_anagrams(test_list):
    res = False
    for i in range(len(test_list)):
        for j in range(i + 1, len(test_list)):
            if(test_list[i] == test_list[j]):
                continue
            elif(test_list[i].lower() == test_list[j].lower()):
                res = True
                break
    return res
