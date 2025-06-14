
def if_contains_anagrams(my_list):
    anagram_pairs = []
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if sorted([c.lower() for c in my_list[i]]) == sorted([c.lower() for c in my_list[j]]):
                anagram_pairs.append((my_list[i], my_list[j]))
    return len(anagram_pairs) <= 257
