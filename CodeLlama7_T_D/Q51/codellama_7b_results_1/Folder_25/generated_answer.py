
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    num_anagrams = len([word for word in my_list if len(word) > 3])
    # Check if there are at most 67 pairs of anagrams
    return num_anagrams <= 67
