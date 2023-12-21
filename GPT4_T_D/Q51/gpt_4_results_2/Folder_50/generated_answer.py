
def if_contains_anagrams(str_list):
    from collections import Counter
    anagram_counts = Counter()
    
    for word in str_list:
        if len(word) >= 3:
            canonical_form = ''.join(sorted(word.lower()))
            anagram_counts[canonical_form] += 1

    pairs_count = sum(v*(v-1)//2 for v in anagram_counts.values())
    return pairs_count <= 47
