
def if_contains_anagrams(strings):
    def to_lower(s):
        return s.lower()

    def is_anagram(s1, s2):
        return sorted(to_lower(s1)) == sorted(to_lower(s2))

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 59:
                    return False

    return True
