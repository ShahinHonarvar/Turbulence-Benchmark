
def if_contains_anagrams(string_list):
    from collections import Counter
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)

    pairs = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and is_anagram(string_list[i].lower(), string_list[j].lower()):
                pairs += 1
    return pairs <= 16
