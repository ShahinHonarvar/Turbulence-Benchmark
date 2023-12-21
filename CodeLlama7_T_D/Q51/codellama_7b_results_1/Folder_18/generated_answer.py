
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    num_anagrams = 0
    for string1 in my_list:
        for string2 in my_list:
            if len(string1) < 3 or len(string2) < 3:
                continue

            if sorted(string1.lower()) == sorted(string2.lower()):
                num_anagrams += 1

    # Return true if there are at most 42 pairs of anagrams in the list; otherwise, return false
    return num_anagrams <= 42
