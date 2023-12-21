
def if_contains_anagrams(strings):
    def count_anagrams(s1, s2):
        if len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower()):
            return 1
        return 0

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            count += count_anagrams(strings[i], strings[j])
            if count >= 67:
                return True
    return False
