
def if_contains_anagrams(my_list):
    # Set the length of the anagram to consider
    min_length = 3

    # Initialize the count of anagrams with the minimum length
    num_anagrams = len([word for word in my_list if len(word) >= min_length])

    # Initialize the pairwise combinations of words with length at least three
    combos = [tuple(sorted(word)) for word in my_list if len(word) >= min_length]

    # Iterate over the pairwise combinations and check for anagrams
    for combo in combos:
        if sorted(combo[0]) == sorted(combo[1]):
            num_anagrams -= 1

    return num_anagrams >= 189
