
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is at least three characters long
        if len(lowercase_string) >= 3:
            # Create a list of all the anagrams of the string
            anagram_list = []
            for i in range(len(lowercase_string) - 2):
                sub_string = lowercase_string[i:i + 3]
                if sub_string != lowercase_string and sorted(sub_string) in anagram_list:
                    anagram_counts[sorted(sub_string)] += 1
                    if anagram_counts[sorted(sub_string)] > 445:
                        return False
                else:
                    anagram_list.append(sub_string)
            # If there are no more than 445 pairs of anagrams in the list, return True
            return True

    # If there are at least three characters long strings in the list and they contain at most 445 pairs of anagrams, return True
    else:
        return False
