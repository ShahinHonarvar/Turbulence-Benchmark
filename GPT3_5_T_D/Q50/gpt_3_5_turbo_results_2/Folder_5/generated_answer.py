
def if_contains_anagrams(string_list):
    from collections import Counter
    counter_dict = {}
    for string in string_list:
        string = string.lower()
        if len(string)>=3:
            counter = Counter(string)
            if counter in counter_dict:
                counter_dict[counter] += 1
            else:
                counter_dict[counter] = 1
    pairs_count = 0
    for count in counter_dict.values():
        pairs_count += count // 2
    return pairs_count >= 21
