
def if_contains_anagrams(string_list):
    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if len(str1) < 3 or len(str2) < 3:
            return False
        if len(str1) != len(str2):
            return False
        char_count = [0] * 26
        for c in str1:
            char_count[ord(c) - 97] += 1
        for c in str2:
            char_count[ord(c) - 97] -= 1
        for count in char_count:
            if count != 0:
                return False
        return True

    count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                count += 1
                if count > 318:
                    return False
    return True
