
def if_contains_anagrams(str_list):
    # Count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list))):
            if sorted(str_list[i]) == sorted(str_list[j]):
                num_anagrams += 1
                if num_anagrams > 68:
                    return False

    return True
