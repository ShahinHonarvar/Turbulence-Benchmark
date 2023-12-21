
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_letters = False
    # Iterate over the list of strings
    for string1 in my_list:
        # Check if the string has at least three letters
        if len(string1) >= 3:
            three_or_more_letters = True
            # Iterate over the rest of the list of strings
            for string2 in my_list[my_list.index(string1) + 1 :]:
                # Check if the two strings are anagrams
                if sorted(string1) == sorted(string2):
                    anagram_count += 1
                    # If there are at least five pairs of anagrams, return True
                    if anagram_count >= 5:
                        return True
    # If there are no three or more letter strings in the list, return False
    if not three_or_more_letters:
        return False
