
def if_contains_anagrams(str_list):
    # count the number of anagram pairs in the list
    pair_count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i].lower()) == sorted(str_list[j].lower()):
                pair_count += 1
                if pair_count >= 246:
                    return True
    return False
