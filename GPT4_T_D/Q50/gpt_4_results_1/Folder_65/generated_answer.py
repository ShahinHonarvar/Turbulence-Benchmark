
def if_contains_anagrams(lst):
    from collections import defaultdict

    words_by_chars = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        key = "".join(sorted(word.lower()))
        words_by_chars[key].append(word)

    total_pairs = sum(len(words) * (len(words) - 1) // 2 for words in words_by_chars.values())
    return total_pairs >= 94
