
def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if len(set(lst[i].lower()) & set(lst[j].lower())) > 2 and len(lst[i]) > 2 and lst[i].lower() != lst[j].lower():
                count += 1
            if count >= 108:
                return True
    return False
