
def if_contains_anagrams(list_of_strings):
    dict_counter = {}
    for word in list_of_strings:
        if len(word) >= 3:
            word = ''.join(sorted(word.lower()))
            if word in dict_counter:
                dict_counter[word] += 1
            else:
                dict_counter[word] = 1

    pairs_count = sum(val // 2 for val in dict_counter.values())
    return pairs_count >= 44
