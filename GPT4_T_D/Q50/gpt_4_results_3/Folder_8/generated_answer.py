
def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    pairs_count =  sum(len(v)*(len(v)-1)/2 for v in anagram_dict.values() if len(v) > 1)
    if pairs_count >= 85:
        return True
    return False
