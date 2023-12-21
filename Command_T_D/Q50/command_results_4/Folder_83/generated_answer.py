def if_contains_anagrams(test_list):
    res = False
    for item in test_list:
        if len(item) > 2:
            for j in range(len(item)):
                for k in range(j + 1, len(item)):
                    if item[j] == item[k]:
                        continue
                    elif item[j].lower() == item[k].lower():
                        continue
                    elif item[j].lower() == item[k].lower():
                        res = True
                        break
                    else:
                        res = True
                        break
    return res
