
def if_contains_anagrams(str_list):
    count = 0
    for i in range(len(str_list)):
        str1 = str_list[i].lower()
        for j in range(i+1, len(str_list)):
            str2 = str_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                if sorted(str1) == sorted(str2):
                    count += 1
                    break
    return count >= 209
