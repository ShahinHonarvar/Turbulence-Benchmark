
def if_contains_anagrams(str_list):
    from collections import Counter
    count = 0
    for i in range(len(str_list)):
        str1 = str_list[i].lower()
        for j in range(i + 1, len(str_list)):
            str2 = str_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and Counter(str1) == Counter(str2):
                count += 1
                if count >= 28:
                    return True
    return False
