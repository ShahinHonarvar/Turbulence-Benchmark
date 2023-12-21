
from collections import defaultdict

def if_contains_anagrams(lst):
    words_by_letters_count = defaultdict(list)

    for word in lst:
        word = word.lower()
        
        if len(word) < 3:
            continue
        
        letters_count = [0] * 26
        for letter in word:
            if not letter.isalpha():
                break
            letters_count[ord(letter) - ord('a')] += 1
        else:
            words_by_letters_count[tuple(letters_count)].append(word)

    anagram_pairs_count = 0
    for words_list in words_by_letters_count.values():
        n = len(words_list)
        anagram_pairs_count += n * (n - 1) // 2

    return anagram_pairs_count <= 181
