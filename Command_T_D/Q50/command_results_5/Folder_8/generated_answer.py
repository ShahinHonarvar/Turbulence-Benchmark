def if_contains_anagrams(test_list):
    res = False
    for first in test_list:
        second_list = []
        for second in test_list:
            if first.lower() == second.lower():
                continue
            elif len(first) == len(second) and len(first) >= 3:
                second_list.append(second)
        if len(second_list) >= 85:
            res = True
            break
    return res
