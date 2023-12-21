
def if_contains_anagrams(my_list):
    # count the number of anagram pairs in the list
    num_pairs = sum([1 for i in range(len(my_list) - 1)) for j in range(i + 1, len(my_list)) if sorted(my_list[i].lower()) == sorted(my_list[j].lower())])
    # return True if there are at most 416 pairs of anagrams in the list
    return num_pairs <= 416
