
def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        return sorted(str1.lower()) == sorted(str2.lower())

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count >= 69:
                    return True
    return False
