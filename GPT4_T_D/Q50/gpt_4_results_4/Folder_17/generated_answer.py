
def if_contains_anagrams(string_list):
    from collections import defaultdict

    anagrams = defaultdict(list)
    for word in string_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)

    pair_count = 0
    for key in anagrams:
        n = len(anagrams[key])
        pair_count += n * (n-1) // 2

    return pair_count >= 97
