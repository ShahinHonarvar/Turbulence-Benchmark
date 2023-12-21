
def if_contains_anagrams(string_list):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]) and len(string_list[i]) >= 3:
                count += 1
                if count >= 153:
                    return True
    return False
