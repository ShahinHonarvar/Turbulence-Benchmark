
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for string in strings:
        # Convert the string to lowercase
        string = string.lower()

        # Check if the string is at least three characters long
        if len(string) < 3:
            continue

        # Split the string into individual letters
        letters = string.split()

        # Create a sorted version of the letters
        sorted_letters = "".join(sorted(letters))

        # Check if the sorted letters are in the dictionary
        if sorted_letters in anagram_counts:
            # Increment the count for this anagram
            anagram_counts[sorted_letters] += 1

        else:
            # Initialize the count for this anagram
            anagram_counts[sorted_letters] = 1

    # Check if there are at most 78 pairs of anagrams in the given list
    return len(anagram_counts) <= 78
