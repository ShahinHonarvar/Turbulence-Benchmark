
def if_contains_anagrams(strings):
    counter = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            counter[sorted_string] = counter.get(sorted_string, 0) + 1
    
    pairs_count = 0
    for count in counter.values():
        pairs_count += count * (count - 1) // 2
    
    return pairs_count >= 50
