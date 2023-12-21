
def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                anagram_count += 1
            if anagram_count > 42:
                return False
    return True if anagram_count <= 42 else False
