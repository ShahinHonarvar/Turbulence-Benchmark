
def if_contains_anagrams(strings):
    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and are_anagrams(strings[i], strings[j]):
                count += 1
                if count >= 78:
                    return True
    return False
