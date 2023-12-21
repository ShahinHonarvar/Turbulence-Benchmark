
def if_contains_anagrams(strings):
    from collections import defaultdict

    # Count the frequencies of sorted strings
    sorted_strings = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_strings["".join(sorted(s.lower()))] += 1

    # Calculate the total number of pairs
    total_pairs = sum(x * (x - 1) // 2 for x in sorted_strings.values())

    return total_pairs >= 19
