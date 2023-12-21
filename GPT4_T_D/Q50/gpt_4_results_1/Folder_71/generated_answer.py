
def if_contains_anagrams(lst):
    seen = dict()
    pairs = 0
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = "".join(sorted(word))
        if sorted_word in seen:
            pairs += seen[sorted_word]
            seen[sorted_word] += 1
        else:
            seen[sorted_word] = 1
    return pairs >= 57
