
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word].append(word)
    count = 0
    for key in anagrams:
        count += len(anagrams[key])*(len(anagrams[key]) - 1) // 2
        if count >= 68:
            return True
    return False
