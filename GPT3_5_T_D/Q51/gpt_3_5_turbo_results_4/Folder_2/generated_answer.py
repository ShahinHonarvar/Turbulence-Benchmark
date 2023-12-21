
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1) == sorted(s2)

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 81:
                    return False
    return True
