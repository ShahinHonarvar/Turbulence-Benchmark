
def if_contains_anagrams(my_list):
    # Initialize a dictionary to store anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for word in my_list:
        # Convert the string to lowercase
        word = word.lower()

        # If the length of the word is greater than or equal to 3
        if len(word) >= 3:
            # Sort the characters in the word
            sorted_chars = "".join(sorted(word))

            # If the sorted string is not already in the dictionary, add it with a count of 1
            if sorted_chars not in anagram_counts:
                anagram_counts[sorted_chars] = 1

            # Otherwise, increment the count by 1
            else:
                anagram_counts[sorted_chars] += 1

    # Check if there are at least 57 pairs of anagrams in the list
    return len([key for key, value in anagram_counts.items() if value >= 2]) >= 57
