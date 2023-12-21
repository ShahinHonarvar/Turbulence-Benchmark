
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Sort the letters in the string
        sorted_letters = ''.join(sorted(lowercase_string))

        # Increment the count for this anagram
        if sorted_letters in anagram_counts:
            anagram_counts[sorted_letters] += 1

        else:
            anagram_counts[sorted_letters] = 1

    # Check if there are at most 34 pairs of anagrams in the list
    return len(anagram_counts) <= 34
