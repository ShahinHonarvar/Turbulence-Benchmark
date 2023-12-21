
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        string = string.lower()

        # Sort the characters in the string
        sorted_string = "".join(sorted(string))

        # Check if the sorted string is already in the anagram counts dictionary
        if sorted_string in anagram_counts:
            # If it is, increment its count
            anagram_counts[sorted_string] += 1

        else:
            # If it's not, add it to the dictionary with a count of 1
            anagram_counts[sorted_string] = 1

    # Iterate over the anagram counts dictionary
    for sorted_string, count in anagram_counts.items():
        # Check if the count is greater than or equal to three
        if count >= 3:
            # If it is, check if there are at most two pairs of anagrams in the list
            pair_count = 0

            # Iterate over the list of strings again
            for string in my_list:
                # Convert the string to lowercase
                string = string.lower()

                # Sort the characters in the string
                sorted_string = "".join(sorted(string))

                # Check if the sorted string is already in the anagram counts dictionary
                if sorted_string in anagram_counts:
                    # If it is, increment its count
                    anagram_counts[sorted_string] += 1

            # Check if there are at most two pairs of anagrams in the list
            pair_count = sum(1 for i in range(len(my_list)) if my_list[i] == string)

            # If there are at most two pairs of anagrams, return true
            if pair_count <= 2:
                return True

    # If there are no pairs of anagrams in the list, return false
    return False
