
def if_contains_anagrams(strings):
    anagram_count = 0
    strings_lowercase = [x.lower() for x in strings]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings_lowercase[i]) >= 3 and sorted(strings_lowercase[i]) == sorted(strings_lowercase[j]):
                anagram_count += 1
                if anagram_count > 289:
                    return False
    return True
