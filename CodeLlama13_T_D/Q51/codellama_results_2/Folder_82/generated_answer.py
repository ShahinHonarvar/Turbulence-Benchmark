
def if_contains_anagrams(my_list):
    anagrams = []
    for i in range(len(my_list)):
        s1 = my_list[i].lower()
        for j in range(i+1, len(my_list)):
            s2 = my_list[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if "".join(sorted(s1)) == "".join(sorted(s2)):
                    anagrams.append((s1, s2))
    return len(anagrams) <= 40
