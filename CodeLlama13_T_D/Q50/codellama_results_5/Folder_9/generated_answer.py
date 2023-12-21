
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs == 66:
                    return True
    return False

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3
