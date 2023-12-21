
def if_contains_anagrams(str_list):
    num_anagrams = 0
    anagram_candidates = set()

    for strng in str_list:
        if len(strng) < 3:
            continue
        for ana in anagram_candidates:
            if sorted(ana.lower()) == sorted(strng.lower()):
                num_anagrams += 1
                break
        anagram_candidates.add(strng.lower())

    return num_anagrams >= 9
