
def if_contains_anagrams(my_list):
    # Count the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                num_pairs += 1
    # Return True if there are at least 60 pairs of anagrams in the list; otherwise return False.
    if num_pairs >= 60:
        return True
    else:
        return False
