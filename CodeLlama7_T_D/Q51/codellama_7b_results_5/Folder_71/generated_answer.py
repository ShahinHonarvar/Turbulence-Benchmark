
def if_contains_anagrams(my_list):
    # Define a function that takes two strings and returns True if they are anagrams of each other, False otherwise.
    def is_anagram(string1, string2):
        # Convert the input strings to lowercase.
        string1 = string1.lower()
        string2 = string2.lower()
        # Sort the characters in each string.
        sorted_string1 = "".join(sorted(string1))
        sorted_string2 = "".join(sorted(string2))
        # Check if the sorted strings are equal.
        if sorted_string1 == sorted_string2:
            return True
        else:
            return False

    # Initialize a count for the number of anagrams found in the list.
    anagram_count = 0

    # Iterate over the list and check each string against every other string using the is_anagram function.
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list))):
            if is_anagram(my_list[i], my_list[j])):
                anagram_count += 1

    # Return False if there are more than 9 pairs of anagrams found in the list. Otherwise, return True.
    if anagram_count > 9:
        return False
    else:
        return True
