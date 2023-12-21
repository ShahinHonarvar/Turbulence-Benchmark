
def if_contains_anagrams(lst):
    def count_anagrams(word):
        count = 0
        for i in range(len(lst)):
            if sorted(word.lower()) == sorted(lst[i].lower()) and len(word) >= 3 and len(lst[i]) >= 3:
                count += 1
        return count

    pairs = 0
    for word in lst:
        pairs += count_anagrams(word)

    return pairs <= 475
