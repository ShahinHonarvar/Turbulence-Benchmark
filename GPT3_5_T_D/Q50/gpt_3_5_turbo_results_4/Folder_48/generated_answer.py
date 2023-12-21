
def if_contains_anagrams(strings):
    counts = {}
    for string in strings:
        if len(string) >= 3:
            lower_string = string.lower()
            sorted_string = ''.join(sorted(lower_string))
            counts[sorted_string] = counts.get(sorted_string, 0) + 1
    pairs = 0
    for count in counts.values():
        pairs += count * (count - 1) // 2
    return pairs >= 219
