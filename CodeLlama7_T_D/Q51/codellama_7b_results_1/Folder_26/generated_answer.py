
def if_contains_anagrams(words):
    # Calculate the anagram counts for each word in the list
    anagram_counts = {}
    for word in words:
        anagrams = get_anagrams(word)
        for anagram in anagrams:
            if anagram not in anagram_counts:
                anagram_counts[anagram] = 1
            else:
                anagram_counts[anagram] += 1
    # Check if there are at most 35 pairs of anagrams in the list
    max_anagram_pairs = 0
    for anagram in anagram_counts:
        if anagram_counts[anagram] > 1:
            max_anagram_pairs += (anagram_counts[anagram] - 1)
    return max_anagram_pairs <= 35
def get_anagrams(word):
    # Return a list of all the anagrams of the given word
    letters = sorted(list(set(word)))
    anagrams = []
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            anagram = ''.join(letters[k] for k in range(i, j))
            if anagram != word:
                anagrams.append(anagram)
    return anagrams
