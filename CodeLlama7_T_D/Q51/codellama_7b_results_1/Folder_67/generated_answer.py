
def if_contains_anagrams(my_list):
    # Initialize the number of anagrams to 0
    num_anagrams = 0
    # Iterate over each string in the list
    for i in range(len(my_list)):
        # Get the current string and its length
        current_string = my_list[i]
        current_length = len(current_string)
        # If the current string is at least three characters long...
        if current_length >= 3:
            # ...create a set of all the English letters
            english_letters = set('abcdefghijklmnopqrstuvwxyz')
            # ...iterate over each letter in the current string
            for j in range(len(current_string)):
                # ...if the current letter is not a space...
                if current_string[j] != ' ':
                    # ...add the letter to the set of English letters
                    english_letters.add(current_string[j])
            # ...check if there are at most 5 pairs of anagrams in the list...
            num_anagrams = sum(1 for i in range(len(my_list)) if i != i + 1 and len(set(my_list[i])) == len(set(my_list[i + 1])))
            # ...if there are at most 5 pairs of anagrams, return True...
            if num_anagrams <= 5:
                return True
