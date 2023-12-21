def if_contains_anagrams(test_list):
    if test_list:
        count = 0
        for j in range(len(test_list) - 1):
            for k in range(j + 1, len(test_list)):
                str1 = test_list[j].lower()
                str2 = test_list[k].lower()
                if str1 == str2:
                    count += 1
                    if count > 94:
                        return False
        return True
    else:
        return False
