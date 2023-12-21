
def if_contains_anagrams(lst):
    count_pairs = 0
    sorted_strings = [''.join(sorted(x.lower())) for x in lst if len(x) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i+1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                count_pairs += 1
                if count_pairs >= 67:
                    return True
    return False
