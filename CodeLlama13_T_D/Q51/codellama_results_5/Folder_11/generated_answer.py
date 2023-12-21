
def if_contains_anagrams(lst):
    # Iterate over the list of strings and count the anagram pairs
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i].lower() == lst[j].lower():
                anagram_pairs += 1
    
    # Return true if there are at most 41 pairs of anagrams, false otherwise
    return anagram_pairs <= 41
