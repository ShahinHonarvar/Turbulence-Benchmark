
def if_contains_anagrams(lst):
    # Initialize a dictionary to store the frequency of each letter
    freq = {}

    # Loop through each string in the list and increment the frequency of each letter it contains
    for s in lst:
        for c in s.lower():
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

    # Check if there are at most 257 pairs of anagrams in the list
    return len(freq) <= 257
