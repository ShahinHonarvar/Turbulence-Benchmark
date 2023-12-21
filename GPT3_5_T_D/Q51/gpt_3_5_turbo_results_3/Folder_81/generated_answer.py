
def if_contains_anagrams(string_list):
    def is_anagram(string1, string2):
        sorted_str1 = ''.join(sorted(string1.lower()))
        sorted_str2 = ''.join(sorted(string2.lower()))
        return sorted_str1 == sorted_str2

    count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if is_anagram(string_list[i], string_list[j]):
                    count += 1
                    if count > 79:
                        return False

    return True
