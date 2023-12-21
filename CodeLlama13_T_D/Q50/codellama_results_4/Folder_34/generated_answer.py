
def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                pairs += 1
                break
    return pairs >= 25

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())
