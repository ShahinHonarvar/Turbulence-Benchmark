
def if_contains_anagrams(my_list):
    # Create a dictionary to store the counts of each anagram
    anagram_counts = {}
    
    # Iterate over the list and count the number of times each anagram appears
    for word in my_list:
        key = ''.join(sorted(word.lower()))
        if key not in anagram_counts:
            anagram_counts[key] = 0
        anagram_counts[key] += 1
    
    # Check if there are at most 22 pairs of anagrams
    return sum(value >= 2 for value in anagram_counts.values()) <= 22
