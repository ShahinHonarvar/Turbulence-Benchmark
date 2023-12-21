
def if_contains_anagrams(list_of_strings):
    from collections import defaultdict
    list_of_strings = [s.lower() for s in list_of_strings if len(s)>2]
 
    ana = defaultdict(list)
    for word in list_of_strings:
        ana[''.join(sorted(word))].append(word)
    
    count_pairs = 0
    for v in ana.values():
        if len(v) > 1:
            count_pairs += len(v) * (len(v) - 1) // 2

    return count_pairs <= 20
