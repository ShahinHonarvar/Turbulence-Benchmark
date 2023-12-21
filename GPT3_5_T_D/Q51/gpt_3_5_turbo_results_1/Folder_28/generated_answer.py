
def if_contains_anagrams(lst):
    def count_letters(s):
        count = [0] * 26
        for char in s.lower():
            if char.isalpha():
                count[ord(char) - ord('a')] += 1
        return tuple(count)

    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        count = count_letters(word)
        if count in anagrams:
            anagrams[count] += 1
        else:
            anagrams[count] = 1

    total_pairs = sum(n // 2 for n in anagrams.values())
    return total_pairs <= 78
