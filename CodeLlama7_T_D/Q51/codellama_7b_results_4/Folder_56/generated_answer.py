
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over each string in the list
    for string in strings:
        # Convert the string to lowercase
        string = string.lower()

        # Check if the string is already in the anagram dictionary
        if string in anagram_counts:
            # Increment the count of the anagram
            anagram_counts[string] += 1
        else:
            # Create a new entry for the anagram in the dictionary
            anagram_counts[string] = 1

    # Iterate over each entry in the anagram dictionary
    for string, count in anagram_counts.items():
        # Check if the string is an anagram of at least three English letters
        if len(string) >= 3 and is_anagram(string):
            # Increment the total count of anagrams found
            total += 1

            # Check if there are more than 11 pairs of anagrams in the list
            if total > 11:
                # Return False to indicate that there are too many anagrams
                return False

    # Return True to indicate that there are at most 11 pairs of anagrams in the list
    return True

def is_anagram(string):
    # Convert the string to a set
    letters = set(string)

    # Check if the set contains only the English letters a-z
    if not letters <= set("abcdefghijklmnopqrstuvwxyz"):
        # Return False to indicate that the string is not an anagram of at least three English letters
        return False

    # Return True to indicate that the string is an anagram of at least three English letters
    return True
