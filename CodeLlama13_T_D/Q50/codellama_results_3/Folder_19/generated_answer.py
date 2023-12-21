
def if_contains_anagrams(str_list):
    count = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            str1 = str_list[i].lower()
            str2 = str_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                if "".join(sorted(str1)) == "".join(sorted(str2)):
                    count += 1
        if count >= 84:
            return True
    return False
