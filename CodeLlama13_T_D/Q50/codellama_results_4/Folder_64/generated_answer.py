
def if_contains_anagrams(strings):
    anagram_pairs = []
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(set(strings[i].lower())) >= 3 and len(set(strings[j].lower())) >= 3:
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                    anagram_pairs.append((strings[i], strings[j]))
    return len(anagram_pairs) >= 5
