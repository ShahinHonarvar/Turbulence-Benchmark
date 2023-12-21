
def if_contains_anagrams(strings):
    from collections import Counter
    anagram_counter = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and strings[i].lower() == strings[j].lower() and Counter(strings[i].lower()) == Counter(strings[j].lower()):
                anagram_counter += 1
                if anagram_counter >= 10:
                    return True
    return False
