
def if_contains_anagrams(str_list):
    anagrams = []
    for str in str_list:
        sorted_str = "".join(sorted(str.lower()))
        if sorted_str not in anagrams:
            anagrams.append(sorted_str)
    return len(anagrams) <= 77
