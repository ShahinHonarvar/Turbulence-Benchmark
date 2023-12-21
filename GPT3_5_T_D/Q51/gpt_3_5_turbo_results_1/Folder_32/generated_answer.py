
def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if len(str1) < 3 or len(str2) < 3:
            return False
        return sorted(str1) == sorted(str2)

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 89:
                    return False
    return True
