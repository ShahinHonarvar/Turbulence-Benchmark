
def if_contains_anagrams(my_list):
    # Check that the input is a list of strings
    if not all(isinstance(s, str) for s in my_list)):
        raise ValueError("Input must be a list of strings")
    # Check that there are at least 246 pairs of anagrams in the list
    pair_count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                pair_count += 1
    return pair_count >= 246
