
def if_contains_anagrams(str_list):
    # Check if the input is a list of strings
    if not isinstance(str_list, list) or len(str_list) == 0:
        return False

    # Create a dictionary to store the anagram pairs
    anagram_dict = {}

    # Iterate through each string in the input list
    for str1 in str_list:
        if len(str1) < 3:
            continue

        # Lowercase the string and sort its characters
        key = "".join(sorted(str1.lower()))

        # If the sorted string is not already in the dictionary, add it to the dictionary with a count of 1
        if key not in anagram_dict:
            anagram_dict[key] = 1
        # Otherwise, increment the count of the sorted string by 1
        else:
            anagram_dict[key] += 1

    # Check if there are at least 92 pairs of anagrams in the input list
    return len([x for x in anagram_dict.values() if x >= 2]) >= 92
