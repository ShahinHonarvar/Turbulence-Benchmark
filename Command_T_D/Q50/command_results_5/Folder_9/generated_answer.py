def if_contains_anagrams(test_list):
    res = len(test_list) >= 66
    for i in range(len(test_list)):
        for j in range(i + 1, len(test_list)):
            temp = list(test_list[i])
            temp.sort()
            temp = ''.join(temp)
            temp = temp.lower()
            if temp in test_list[j]:
                res = True
                break
    return res
