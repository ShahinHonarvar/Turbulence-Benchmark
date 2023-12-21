
def if_contains_anagrams(lst):
    lower_list = [i.lower() for i in lst]
    word_pairs = []
    for i in range(len(lower_list)):
        for j in range(i + 1, len(lower_list)):
            if len(lower_list[i]) >= 3 and sorted(lower_list[i]) == sorted(lower_list[j]):
                word_pairs.append((lower_list[i], lower_list[j]))
    return len(word_pairs) >= 5
