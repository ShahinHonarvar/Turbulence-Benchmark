
def if_contains_anagrams(string_list):
    # count the number of anagrams in the list
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list))):
            if sorted(string_list[i].lower()) == sorted(string_list[j].lower()):
                anagram_count += 1

    # check if there are at least 39 pairs of anagrams in the list
    if anagram_count >= 39:
        return True
    else:
        return False
