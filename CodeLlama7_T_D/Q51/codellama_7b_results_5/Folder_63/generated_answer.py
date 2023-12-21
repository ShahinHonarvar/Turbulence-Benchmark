
def if_contains_anagrams(my_list):
    # Get the number of anagrams in the list
    num_anagrams = len([x for x in my_list if x.isalpha()])
    # Check if there are at most 423 pairs of anagrams in the list
    return num_anagrams <= 423
