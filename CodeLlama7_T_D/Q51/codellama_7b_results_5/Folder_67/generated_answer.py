
def if_contains_anagrams(my_list):
    # create a counter for each letter
    letter_counter = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
    # iterate over the list of strings
    for string in my_list:
        # convert the string to lowercase
        string = string.lower()
        # iterate over each letter in the string
        for letter in string:
            # increment the counter for the current letter
            letter_counter[letter] += 1
    # check if there are at most 5 pairs of anagrams in the list
    return len([(a, b) for a in letter_counter for b in letter_counter if a != b and a + b == 2 * (a + b)]) <= 5
