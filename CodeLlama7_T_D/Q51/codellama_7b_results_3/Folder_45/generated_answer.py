
def if_contains_anagrams(words):
    # Calculate the number of pairs of anagrams in the list
    num_pairs = sum([1 for i in range(len(words)-1) for j in range(i+1, len(words)) if sorted(words[i]) == sorted(words[j])])
    # If there are at most 464 pairs of anagrams, return True
    return num_pairs <= 464
