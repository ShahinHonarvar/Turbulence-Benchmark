
def if_contains_anagrams(strings):
    def is_anagram(string1, string2):
        return sorted(string1.lower()) == sorted(string2.lower())

    pairs_count = 0

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and is_anagram(strings[i], strings[j]):
                pairs_count += 1

                if pairs_count >= 106:
                    return True

    return False
