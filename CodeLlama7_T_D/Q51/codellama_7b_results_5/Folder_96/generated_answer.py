
def if_contains_anagrams(my_list):
    # Check if there are at most 2 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(my_list) - 1)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j]):
                num_pairs += 1
                if num_pairs > 2:
                    return False

    # Check if the anagrams have at least three letters

    for word in my_list:
        if len(word) < 3:
            return False

    # Return true if there are at most 2 pairs of anagrams in the given list

    return True
