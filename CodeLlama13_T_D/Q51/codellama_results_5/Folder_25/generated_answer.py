
def if_contains_anagrams(my_list):
    return all(len(i) >= 3 and len(set(i)) == len(i) for i in my_list) and sum(1 for i in my_list if ''.join(sorted(i.lower())) in [j for j in set((''.join(sorted(k.lower()))))]) <= 67
