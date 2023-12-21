def if_contains_anagrams(str_list):
    return sum(
        1
        for s1, s2 in zip(str_list, str_list)
        if s1 == s2
        for i in range(len(s1) - 2)
        for j in range(len(s2) - 2)
        if s1[i] == s2[j]
    ) >= 69
