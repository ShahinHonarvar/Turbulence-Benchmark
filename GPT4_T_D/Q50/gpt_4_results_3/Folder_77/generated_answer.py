
def if_contains_anagrams(list_of_strings):
    anagram_dictionary = {}
    for item in list_of_strings:
        item = item.lower()
        if len(item) >= 3:
            sorted_item = ''.join(sorted(item))
            if sorted_item in anagram_dictionary:
                anagram_dictionary[sorted_item].append(item)
            else:
                anagram_dictionary[sorted_item] = [item]
    anagram_pairs = 0
    for v in anagram_dictionary.values():
        if len(v) >= 2:
            anagram_pairs += len(v)*(len(v)-1)//2
    if anagram_pairs >= 209:
        return True
    return False
