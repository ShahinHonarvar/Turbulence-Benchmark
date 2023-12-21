
def if_contains_anagrams(my_list):
    # Get the list of anagrams
    anagram_pairs = []
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                anagram_pairs.append((i, j)))
    # Check if there are more than 10 pairs of anagrams
    if len(anagram_pairs) > 10:
        return False

    # Check if all the anagrams have at least three letters
    for pair in anagram_pairs:
        if len(my_list[pair[0]]) < 3 or len(my_list[pair[1]]) < 3:
            return False

    # Check if there are any repeated anagrams
    for pair in anagram_pairs:
        if pair in anagram_pairs[:pair[0]]:
            return False

    # If all the conditions above are met, then the list contains at most 10 pairs of anagrams
    return True
