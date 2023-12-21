
def if_contains_anagrams(string_list):
    counts = {}
    for string in string_list:
        normalized_string = string.lower()
        if len(normalized_string) >= 3:
            counts[normalized_string] = counts.get(normalized_string, 0) + 1
    pairs = 0
    for count in counts.values():
        pairs += count * (count - 1) // 2
    return pairs >= 39
