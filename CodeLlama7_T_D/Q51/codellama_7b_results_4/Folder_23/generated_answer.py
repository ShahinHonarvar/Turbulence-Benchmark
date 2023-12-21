
def if_contains_anagrams(my_list):
    # count the number of anagrams in the list
    anagram_count = 0
    for i in range(len(my_list) - 1)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                anagram_count += 1
    # check if the number of anagrams is less than or equal to 49
    return anagram_count <= 49
