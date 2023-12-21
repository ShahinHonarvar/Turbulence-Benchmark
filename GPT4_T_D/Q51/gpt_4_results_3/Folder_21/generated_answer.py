
def if_contains_anagrams(lst):
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word)>=3]
    count_dict = {}
    for word in sorted_words:
        if word in count_dict:
            count_dict[word] += 1 if count_dict[word] < 26 else 0
        else:
            count_dict[word] = 1
    for word in count_dict:
        if count_dict[word] > 2:
            return False
    return True
