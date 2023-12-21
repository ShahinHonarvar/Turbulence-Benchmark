
def if_contains_anagrams(string_list):
    def is_anagram(string1, string2):
        return sorted(string1.lower()) == sorted(string2.lower())

    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                anagram_count += 1
                if anagram_count > 58:
                    return False
    return True
