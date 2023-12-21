
def if_contains_anagrams(str_list):
    # Check if there are at most 39 pairs of anagrams in the list
    num_anagrams = 0
    for i in range(len(str_list)):
        str1 = str_list[i]
        for j in range(i+1, len(str_list)):
            str2 = str_list[j]
            if sorted(str1.lower()) == sorted(str2.lower()):
                num_anagrams += 1
                if num_anagrams > 39:
                    return False

    return True
