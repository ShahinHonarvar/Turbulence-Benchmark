
def if_contains_anagrams(lst):
    counts = dict()
    for word in lst:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word not in counts:
                counts[sorted_word] = 1
            else:
                counts[sorted_word] += 1

    pairs = sum(count // 2 for count in counts.values())
    return pairs >= 28
