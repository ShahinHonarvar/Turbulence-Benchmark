
def if_contains_anagrams(string_list):
    pairs = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            s1 = string_list[i].lower()
            s2 = string_list[j].lower()
            if s1 != s2 and sorted(s1) == sorted(s2):
                pairs += 1
    return pairs <= 89
