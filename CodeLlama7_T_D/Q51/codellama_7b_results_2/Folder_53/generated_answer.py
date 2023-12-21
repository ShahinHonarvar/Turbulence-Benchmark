
def if_contains_anagrams(my_list):
    # Create a set of all anagrams in the list
    anagram_set = {i for i in my_list if ''.join(sorted(i)) == ''.join(sorted(j))) for j in my_list}
    # Check if there are at most 8 pairs of anagrams in the set
    num_pairs = len(anagram_set) - len(my_list) + 1
    return num_pairs <= 8
