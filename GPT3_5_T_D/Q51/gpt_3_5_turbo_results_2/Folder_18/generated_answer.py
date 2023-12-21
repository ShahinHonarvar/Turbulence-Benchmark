
def if_contains_anagrams(strings):
    pairs = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        pairs[sorted_string] = pairs.get(sorted_string, 0) + 1
        if pairs[sorted_string] == 2:
            count += 1
        elif pairs[sorted_string] == 3:
            count -= 1
    return count <= 42
