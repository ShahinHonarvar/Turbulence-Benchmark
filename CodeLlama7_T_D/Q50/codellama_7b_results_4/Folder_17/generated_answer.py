
def if_contains_anagrams(string_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over each string in the list
    for string in string_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # If the length of the string is at least 3, continue
        if len(lowercase_string) >= 3:
            # Sort the characters in the string
            sorted_characters = "".join(sorted(lowercase_string))

            # If the anagram count for the sorted string is greater than 0, add it to the total anagram count
            if sorted_characters in anagram_counts:
                anagram_counts[sorted_characters] += 1

            # Otherwise, set the anagram count for the sorted string to 1
            else:
                anagram_counts[sorted_characters] = 1

    # If there are at least 97 pairs of anagrams in the list, return True
    if sum([v > 0 for v in anagram_counts.values()]) >= 97:
        return True

    # Otherwise, return False
    else:
        return False
