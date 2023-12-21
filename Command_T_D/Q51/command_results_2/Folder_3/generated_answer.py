import re
def if_contains_anagrams(test_list):
    test_list = sorted(test_list)
    test_list.sort()
    count = 0
    for x in range(len(test_list)):
        for y in range(x + 1, len(test_list)):
            if test_list[x] == test_list[y]:
                continue
            elif len(test_list[x]) < len(test_list[y]):
                continue
            elif test_list[x] == test_list[y].lower():
                count += 1
    return count <= 66
