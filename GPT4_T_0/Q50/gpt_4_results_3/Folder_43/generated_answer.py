
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key])*(len(anagrams[key])-1)//2
        if count >= 61:
            return True
    return False
