
def if_contains_anagrams(my_list):
    # convert all strings to lowercase
    my_list = [s.lower() for s in my_list]
    
    # count the frequency of each letter in the list
    freq = {}
    for s in my_list:
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
    
    # check if there are at most 58 pairs of anagrams in the list
    count = 0
    for s1, s2 in combinations(my_list, 2):
        if sorted(s1) == sorted(s2):
            count += 1
    
    return count <= 58
