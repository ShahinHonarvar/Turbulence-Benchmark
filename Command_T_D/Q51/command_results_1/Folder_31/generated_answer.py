import collections
def if_contains_anagrams(test_list):
    res = 0
    for i in test_list:
        for j in test_list:
            if(i == j):
                continue
            elif(i in j or j in i):
                res += 1
            elif(i in j[1:]):
                res += 1
            elif(j in i[1:]):
                res += 1
            elif(i[0] in j):
                res += 1
            elif(j[0] in i):
                res += 1
            elif(i[1] in j):
                res += 1
            elif(j[1] in i):
                res += 1
            elif(i[2] in j):
                res += 1
            elif(j[2] in i):
                res += 1
    return res <= 65
