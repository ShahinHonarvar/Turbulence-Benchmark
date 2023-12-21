
def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    count = 0
    lst_lower = [x.lower() for x in lst if len(x) >= 3]
    for i in range(len(lst_lower)):
        for j in range(i+1, len(lst_lower)):
            if is_anagram(lst_lower[i], lst_lower[j]):
                count += 1
                if count > 392:
                    return False
    return True
