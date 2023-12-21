
def if_contains_anagrams(my_list):
    # Convert all strings to lowercase
    my_list = [s.lower() for s in my_list]
    # Create a dictionary to store the number of anagrams for each string length
    anagram_counts = {}

    for string in my_list:
        # Get the length of the string
        length = len(string)

        if length not in anagram_counts:
            # If the string length is not in the dictionary, set its value to 1 (i.e., there is only one anagram of this length)
            anagram_counts[length] = 1

        else:
            # Otherwise, increment the number of anagrams for this string length by 1
            anagram_counts[length] += 1

    # Check if there are at most 20 pairs of anagrams in the given list
    return sum(anagram_counts.values()) <= 20 * len(my_list)
