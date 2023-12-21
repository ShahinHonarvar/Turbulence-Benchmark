
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for string in strings:
        # Convert the string to lowercase
        string = string.lower()

        # Sort the characters of the string
        sorted_string = "".join(sorted(string))

        # Increment the count of the anagram
        if sorted_string in anagram_counts:
            anagram_counts[sorted_string] += 1

        else:
            anagram_counts[sorted_string] = 1

    # Check if there are at most 2 pairs of anagrams in the given list
    for sorted_string, count in anagram_counts.items():
        if count > 2:
            return False

    return True
