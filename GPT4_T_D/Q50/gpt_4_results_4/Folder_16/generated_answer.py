
def if_contains_anagrams(input_list):
    anagram_count = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if len(input_list[i]) > 2 and sorted(input_list[i].lower()) == sorted(input_list[j].lower()):
                anagram_count += 1
    return anagram_count >= 155
