
def if_contains_anagrams(my_list):
    # Create a set of all anagram-able strings in the list
    anagram_strings = set()
    for string in my_list:
        # Convert the string to lowercase and remove whitespace
        cleaned_string = string.lower().strip()
        # Only consider strings that are at least 3 characters long
        if len(cleaned_string) < 3:
            continue

        # Create a list of all anagram-able substrings in the string
        substring_list = []
        for i in range(len(cleaned_string) - 2):
            substring_list.append(cleaned_string[i:i + 3])
        # Add each substring to the set of all anagram-able strings
        for substring in substring_list:
            anagram_strings.add(substring)
    # Check if there are at most 11 pairs of anagrams in the list
    return len(anagram_strings) <= 11
