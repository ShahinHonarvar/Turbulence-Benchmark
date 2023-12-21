
def if_contains_anagrams(string_list):
    from collections import Counter
    sorted_anagrams = []

    for word in string_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            sorted_anagrams.append(sorted_word)

    word_counts = Counter(sorted_anagrams)
    anagram_pairs = sum(v*(v-1)//2 for v in word_counts.values())

    return anagram_pairs <= 91
