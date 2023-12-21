
def if_contains_anagrams(str_list):
    def count_anagrams(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        sorted_str1 = sorted(str1.lower())
        sorted_str2 = sorted(str2.lower())
        return sorted_str1 == sorted_str2

    count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if count_anagrams(str_list[i], str_list[j]):
                count += 1
                if count > 74:
                    return False
    return True
