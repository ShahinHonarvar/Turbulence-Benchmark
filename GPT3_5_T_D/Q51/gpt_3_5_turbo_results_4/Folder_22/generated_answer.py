
def if_contains_anagrams(string_list):
    from collections import Counter
    count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            s1 = string_list[i].lower()
            s2 = string_list[j].lower()
            if sorted(list(s1)) == sorted(list(s2)) and len(s1) >= 3:
                count += 1
    return count <= 14
