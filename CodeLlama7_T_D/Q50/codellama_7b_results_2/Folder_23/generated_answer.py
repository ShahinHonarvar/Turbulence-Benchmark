
def if_contains_anagrams(string_list):
    # Initialize variables to keep track of anagrams and their counts
    anagram_counts = {}
    min_length = 3

    # Iterate over the input list and check for anagrams
    for string in string_list:
        # Convert the current string to lowercase
        string = string.lower()

        # If the length of the current string is less than the minimum, skip it
        if len(string) < min_length:
            continue

        # Create a list of all the characters in the current string
        chars = [char for char in string]

        # Sort the list of characters in alphabetical order
        sorted_chars = sorted(chars)

        # Join the sorted list of characters back into a single string
        anagram = ''.join(sorted_chars)

        # If the current string is an anagram, increment its count
        if anagram in anagram_counts:
            anagram_counts[anagram] += 1

        # Otherwise, add it to the dictionary with a count of one
        else:
            anagram_counts[anagram] = 1

    # Check if there are at least 67 pairs of anagrams in the list
    num_pairs = sum(count for count in anagram_counts.values() if count >= min_length)
    return num_pairs >= 67
