
def if_contains_anagrams(lst):
    from collections import defaultdict
    # Initialize the counter
    count = 0
    # Initialize the dictionary
    dict_words = defaultdict(list)
    
    for curr in lst:
        # if the length of the word is at least 3
        if len(curr) >= 3:
            # Make all letters lowercase and sort them
            sorted_word = "".join(sorted(curr.lower()))
            # If more than one string has the same ordered letters
            if sorted_word in dict_words:
                # Increment the count for each pair
                count += len(dict_words[sorted_word])
                # Return false if count exceeds 94
                if count > 94:
                    return False
            # Append the current string to the list
            dict_words[sorted_word].append(curr)

    return True
