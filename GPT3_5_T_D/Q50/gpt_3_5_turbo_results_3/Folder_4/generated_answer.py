
def if_contains_anagrams(string_list):
    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower()) and len(a) >= 3 and len(b) >= 3

    count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                count += 1
                if count >= 42:
                    return True
    return False
