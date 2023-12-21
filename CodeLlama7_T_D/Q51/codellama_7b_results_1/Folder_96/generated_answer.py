
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagrams and pairs
    anagrams = set()
    pairs = []

    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a valid anagram by comparing its length to 3
        if len(lowercase_string) >= 3:
            # Create a sorted copy of the string
            sorted_string = "".join(sorted(lowercase_string))

            # Check if the sorted string is already in the set of anagrams
            if sorted_string not in anagrams:
                # Add the sorted string to the set of anagrams
                anagrams.add(sorted_string)

                # Check if there are at most 2 pairs of anagrams in the given list by comparing the length of the list of pairs to 2
                if len(pairs) <= 2:
                    # Add a pair consisting of the original string and its sorted copy to the list of pairs
                    pairs.append((string, lowercase_string))
        else:
            # Return false if the string is not a valid anagram
            return False

    # If there are at most 2 pairs of anagrams in the given list, return true
    if len(pairs) <= 2:
        return True

    # Otherwise, return false
    else:
        return False
