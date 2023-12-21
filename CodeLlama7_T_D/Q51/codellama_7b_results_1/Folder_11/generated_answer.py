
def if_contains_anagrams(my_list):
    # Check if there are at most 41 pairs of anagrams in the given list
    count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                count += 1
                if count > 41:
                    return False
    return True
