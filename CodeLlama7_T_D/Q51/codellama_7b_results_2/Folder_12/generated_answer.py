
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Sort the lowercase string and use it as a key in the anagram counts dictionary
        sorted_string = "".join(sorted(lowercase_string))
        if sorted_string not in anagram_counts:
            anagram_counts[sorted_string] = 1

        else:
            anagram_counts[sorted_string] += 1

    # Check if there are at most 92 pairs of anagrams in the list
    return len(anagram_counts) <= 92
