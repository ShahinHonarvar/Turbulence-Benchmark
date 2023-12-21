
def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                anagrams[sorted_word] += 1

    count = 0
    for val in anagrams.values():
        if val > 1:
            count += val*(val-1)//2 # number of pairs in a group
        if count >= 57:
            return True
    return False
