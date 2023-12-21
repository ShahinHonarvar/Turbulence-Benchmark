
def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) > 2]
    unique_strings = set(sorted_strings)
    anagrams_count = 0
    for unique_string in unique_strings:
        count = sorted_strings.count(unique_string)
        anagrams_count += count * (count - 1) // 2
        if anagrams_count >= 74:
            return True
    return False
