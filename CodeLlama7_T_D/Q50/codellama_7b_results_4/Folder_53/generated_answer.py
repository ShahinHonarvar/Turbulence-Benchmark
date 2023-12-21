
def if_contains_anagrams(my_list):
    anagram_count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                anagram_count += 1
                if anagram_count >= 11:
                    return True
    return False
