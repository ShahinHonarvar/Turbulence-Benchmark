
def if_contains_anagrams(string_list):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    n = len(string_list)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and is_anagram(string_list[i], string_list[j]):
                cnt += 1
                if cnt > 78:
                    return False
    return True
