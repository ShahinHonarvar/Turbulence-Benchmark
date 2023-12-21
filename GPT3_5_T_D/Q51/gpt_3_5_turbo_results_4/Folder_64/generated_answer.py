
def if_contains_anagrams(string_list):
    from collections import Counter

    def is_anagram(string1, string2):
        string1 = string1.lower()
        string2 = string2.lower()
        return Counter(string1) == Counter(string2)

    pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if is_anagram(string_list[i], string_list[j]):
                    pairs += 1
                    if pairs > 59:
                        return False
    return True
