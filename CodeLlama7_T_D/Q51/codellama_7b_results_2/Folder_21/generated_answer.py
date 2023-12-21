
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the input list
    for string in strings:
        # Convert the string to lowercase
        # This will make the comparison case-insensitive
        lowercase_string = string.lower()

        # Check if there are at least three characters in the string
        if len(lowercase_string) >= 3:
            # Create a list of tuples, where each tuple represents an anagram
            anagrams = [(lowercase_string[i], lowercase_string[j]) for i in range(len(lowercase_string) - 1) for j in range(i + 1, len(lowercase_string))]

            # Loop through each anagram in the list
            for anagram in anagrams:
                # If the anagram is a valid anagram, increment the count for that anagram
                if set(anagram[0]) == set(anagram[1]):
                    key = ''.join(sorted(anagram[0]))
                    if key in anagram_counts:
                        anagram_counts[key] += 1
                    else:
                        anagram_counts[key] = 1

            # Check if there are at most 26 pairs of anagrams in the list
            if len(anagram_counts) <= 26:
                return True

    return False
