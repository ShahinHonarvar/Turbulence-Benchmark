
def if_contains_anagrams(my_list):
    pairs = []
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                pairs.append((i, j))
    return len(pairs) >= 24
