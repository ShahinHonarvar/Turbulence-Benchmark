
def if_contains_anagrams(string_list):
    import itertools
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    for i in range(len(string_list) - 1):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if is_anagram(string_list[i], string_list[j]):
                    count += 1
                    if count > 70:
                        return False
    return True
