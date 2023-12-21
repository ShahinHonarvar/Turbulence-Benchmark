
def if_contains_anagrams(lst):
    def count_occurrences(s):
        count = [0] * 26
        for char in s:
            count[ord(char.lower()) - ord('a')] += 1
        return tuple(count)

    counts = {}
    for word in lst:
        if len(word) >= 3:
            count = count_occurrences(word)
            counts[count] = counts.get(count, 0) + 1

    num_anagrams = 0
    for count in counts.values():
        num_anagrams += count * (count - 1) // 2

    return num_anagrams >= 209
