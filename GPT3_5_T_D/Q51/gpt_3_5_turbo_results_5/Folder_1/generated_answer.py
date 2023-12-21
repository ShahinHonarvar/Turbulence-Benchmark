
def if_contains_anagrams(string_list):
    def is_anagram(s1, s2):
        if len(s1) != len(s2):
            return False
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    n = len(string_list)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if is_anagram(string_list[i], string_list[j]):
                count += 1
                if count > 30:
                    return False

    return True
