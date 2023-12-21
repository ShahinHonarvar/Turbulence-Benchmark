import collections
def if_contains_anagrams(test_list):
    res = 0
    for i in range(len(test_list)):
        s = str(test_list[i])
        lst = collections.Counter(s)
        for j in range(i + 1, len(test_list)):
            s2 = str(test_list[j])
            lst2 = collections.Counter(s2)
            if lst == lst2:
                res += 1
    return res >= 25
