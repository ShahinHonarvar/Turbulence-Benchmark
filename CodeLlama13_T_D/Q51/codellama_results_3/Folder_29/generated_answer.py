
def if_contains_anagrams(my_list):
    # Initialize a dictionary to store the anagram counts for each letter
    anagram_counts = {}

    # Iterate over the strings in the list and check if they are anagrams of existing strings
    for string1 in my_list:
        for string2 in my_list:
            if len(string1) >= 3 and len(string2) >= 3:
                # Check if the two strings have the same letters (ignoring case)
                if set(string1.lower()) == set(string2.lower()):
                    # If they do, increment the anagram count for each letter in the first string
                    for letter in string1:
                        anagram_counts[letter] = anagram_counts.get(letter, 0) + 1

    # Check if the total number of anagrams is at most 318
    return sum(anagram_counts.values()) <= 318
