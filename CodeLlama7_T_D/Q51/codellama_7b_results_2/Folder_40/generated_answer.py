
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Create a set to store the anagram pairs
    anagram_pairs = set()

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a valid anagram
        if len(lowercase_string) < 3:
            continue

        # Generate all possible anagrams of the string
        for anagram in generate_anagrams(lowercase_string):
            # Add the anagram pair to the set
            anagram_pairs.add((string, anagram))

    # Check if there are at most 29 pairs of anagrams in the list
    return len(anagram_pairs) <= 29
