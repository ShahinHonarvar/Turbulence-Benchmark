
def if_contains_anagrams(string_list):
    anagram_pairs = []
    string_list = [''.join(sorted(word.lower())) for word in string_list if len(word)>=3]

    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if string_list[i] == string_list[j] and (i, j) not in anagram_pairs:
                 anagram_pairs.append((i, j))

    if len(anagram_pairs) <= 25:
        return True
    else:
        return False
