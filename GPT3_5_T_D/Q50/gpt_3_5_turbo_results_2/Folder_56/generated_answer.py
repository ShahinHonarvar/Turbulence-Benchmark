
def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and lst[i].lower() == lst[j].lower():
                count += 1
    if count >= 77:
        return True
    else:
        return False
