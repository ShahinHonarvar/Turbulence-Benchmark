
def if_contains_anagrams(my_list):
    # create a set of all the anagrams in the list
    anagram_set = {tuple(sorted(word)) for word in my_list}
    # check if there are at most 89 pairs of anagrams in the list
    return len(anagram_set) <= 89
