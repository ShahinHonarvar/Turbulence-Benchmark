
def if_contains_anagrams(strings):
    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count > 50:
                    return False

    return True
