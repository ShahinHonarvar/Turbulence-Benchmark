
from collections import defaultdict

def if_contains_anagrams(str_list):
    # Count the anagrams
    ana_count = defaultdict(int)
    for word in str_list:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            ana_count[sorted_word] += 1

    # Calculate the pairs of anagrams
    total_pairs = sum((count * (count-1)) // 2 for count in ana_count.values())

    return total_pairs <= 210
