
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Get the letters of the current string in lowercase
        letters = [char.lower() for char in string]

        # Sort the letters to form an anagram
        sorted_letters = "".join(sorted(letters))

        # If the anagram exists in the dictionary, increment its count
        if sorted_letters in anagram_counts:
            anagram_counts[sorted_letters] += 1

        # Otherwise, add it to the dictionary with a count of 1
        else:
            anagram_counts[sorted_letters] = 1

    # Check if there are at most 173 pairs of anagrams in the list
    return sum(count for count in anagram_counts.values() if count > 1) <= 173
