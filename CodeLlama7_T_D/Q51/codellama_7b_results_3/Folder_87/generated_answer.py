
def if_contains_anagrams(my_list):
    # Get all anagram pairs in the list
    anagram_pairs = []
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                anagram_pairs.append((my_list[i], my_list[j]))
    # Check if there are more than 392 pairs of anagrams in the list
    return len(anagram_pairs) <= 392
