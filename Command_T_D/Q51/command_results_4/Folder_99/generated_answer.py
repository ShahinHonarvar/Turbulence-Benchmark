import collections
def if_contains_anagrams(test_list):
    test_dict = {}
    for element in test_list:
        temp_dict = {}
        for i in range(len(element)-2):
            if element[i] in temp_dict:
                temp_dict[element[i]] += 1
            else:
                temp_dict[element[i]] = 1
        test_dict.update(temp_dict)
    return True if len(test_dict) <= 93 else False
