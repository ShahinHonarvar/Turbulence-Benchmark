
def if_contains_anagrams(strings_list):
    from collections import defaultdict

    anagrams = defaultdict(list)
    for word in strings_list:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            anagrams[key].append(word)

    pairs_count = 0
    for key, words in anagrams.items():
        pairs_count += (len(words) * (len(words) - 1)) // 2

    return pairs_count >= 65
