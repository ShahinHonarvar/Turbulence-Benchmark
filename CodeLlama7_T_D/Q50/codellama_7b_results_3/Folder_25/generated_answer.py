
def if_contains_anagrams(str_list):
    # Check if there are at least 14 pairs of anagrams in the given list
    pair_count = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]):
                pair_count += 1
                if pair_count >= 14:
                    return True

    return False
