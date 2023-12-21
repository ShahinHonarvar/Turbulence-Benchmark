
def if_contains_anagrams(s_list):
    anagrams_counter = 0
    word_count = len(s_list)
    for i in range(word_count):
        for j in range(i+1, word_count):
            if len(s_list[i]) >= 3 and sorted(s_list[i].lower()) == sorted(s_list[j].lower()):
                anagrams_counter += 1
    if anagrams_counter >= 78:
        return True
    else:
        return False
