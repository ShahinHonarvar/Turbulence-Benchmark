
def if_contains_anagrams(my_list):
    anagrams = []
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if "".join(sorted(my_list[i].lower())) == "".join(sorted(my_list[j].lower())):
                anagrams.append((my_list[i], my_list[j]))
    return len(anagrams) <= 25
