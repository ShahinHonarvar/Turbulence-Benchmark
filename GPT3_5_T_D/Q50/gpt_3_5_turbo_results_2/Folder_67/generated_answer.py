
def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                count += 1
                if count >= 41:
                    return True
    return False
