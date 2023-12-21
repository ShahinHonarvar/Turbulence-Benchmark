
def if_contains_anagrams(my_list):
    # Get the list of anagram pairs
    anagram_pairs = []
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                anagram_pairs.append((i, j))
    # Check the number of anagram pairs
    if len(anagram_pairs) <= 69:
        return True

    else:

        return False
