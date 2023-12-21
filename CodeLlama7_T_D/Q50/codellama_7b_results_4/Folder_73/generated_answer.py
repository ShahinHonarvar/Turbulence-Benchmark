
def if_contains_anagrams(string_list):
    # check if the input is a list of strings
    if not all(isinstance(s, str) for s in string_list)):
        raise TypeError("Input must be a list of strings.")
    # count the number of anagram pairs in the list
    num_pairs = 0
    for i in range(len(string_list) - 1):
        for j in range(i + 1, len(string_list))):
            if sorted(string_list[i].lower()) == sorted(string_list[j].lower())):
                num_pairs += 1
    # return True if there are at least 91 anagram pairs in the list; False otherwise
    return num_pairs >= 91
