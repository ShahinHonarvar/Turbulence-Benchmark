
def if_contains_anagrams(lst):
    return sum(1 for i in range(len(lst)) for j in range(i+1, len(lst)) if sorted(lst[i].lower()) == sorted(lst[j].lower())) <= 401
