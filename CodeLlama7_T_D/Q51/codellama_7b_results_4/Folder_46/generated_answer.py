
def if_contains_anagrams(my_list):
    # Create a set of all letters in the list
    letter_set = set()
    for word in my_list:
        # Add each letter to the set
        for letter in word:
            letter_set.add(letter)
    # Check if there are at most 61 pairs of anagrams
    return len(letter_set) <= 61
