
def if_contains_anagrams(my_list):
    pairs = []
    for i in range(len(my_list)):
        if len(my_list[i]) >= 3:
            my_list[i] = sorted(my_list[i].lower())
            pairs.append([my_list[i], my_list[:]])
    return len([x for x in pairs if x[0] != x[1] and x[0] != x[2]]) >= 22
