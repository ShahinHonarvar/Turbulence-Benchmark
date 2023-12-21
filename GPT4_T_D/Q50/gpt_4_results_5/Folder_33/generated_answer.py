
from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    # Ignore case and sort characters in strings for comparison
    normalized_strings = [''.join(sorted(s.lower())) for s in list_of_strings if len(s) >= 3]
    
    # Count occurrences of each unique string
    string_counts = defaultdict(int)
    for s in normalized_strings:
        string_counts[s] += 1
    
    # Check if there are at least 140 pairs of anagrams
    pair_count = sum([count * (count - 1) // 2 for count in string_counts.values()])
    return pair_count >= 140
