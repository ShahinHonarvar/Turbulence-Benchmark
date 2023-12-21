
def if_contains_anagrams(lst):
    from collections import defaultdict

    def sorted_words(word):
        return ''.join(sorted(word))

    count_anagrams = defaultdict(list)
    
    for word in lst:
        if len(word) >= 3:
            count_anagrams[sorted_words(word.lower())].append(word)

    valid_anagram_pairs = sum([len(words) * (len(words) - 1) // 2 for words in count_anagrams.values() if len(words)>1])

    return valid_anagram_pairs <= 9
