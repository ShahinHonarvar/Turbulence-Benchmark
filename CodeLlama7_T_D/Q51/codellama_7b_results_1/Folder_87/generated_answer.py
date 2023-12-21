
def if_contains_anagrams(my_list):
    # Convert the list of strings to lowercase
    my_list = [s.lower() for s in my_list]
    # Get a list of all anagram pairs in the list
    anagram_pairs = [(s1, s2) for s1 in my_list for s2 in my_list if s1 != s2 and sorted(s1) == sorted(s2)]
    # Count the number of anagram pairs that are at least three letters long
    num_anagrams = len([(s1, s2) for (s1, s2) in anagram_pairs if len(s1) >= 3 and len(s2) >= 3])
    # Return True if there are at most 392 anagram pairs in the list, otherwise return False
    return num_anagrams <= 392
