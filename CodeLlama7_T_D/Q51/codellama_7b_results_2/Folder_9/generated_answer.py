
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    min_length = 3

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        curr_string = my_list[i]

        # Check if the current string is an anagram of another string in the list
        for j in range(len(my_list)):
            # Skip the current string and the string at index 'j'
            if i == j:
                continue

            # Get the other string
            other_string = my_list[j]

            # Check if the two strings are anagrams of each other
            if is_anagram(curr_string, other_string):
                # Increment the number of pairs found
                num_pairs += 1

    # Return true if there are at most 475 pairs of anagrams in the given list; otherwise, return false.
    return num_pairs <= 475

# Check if two strings are anagrams of each other
def is_anagram(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Sort the characters in both strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    # Check if the two sorted strings are equal
    return str1 == str2
