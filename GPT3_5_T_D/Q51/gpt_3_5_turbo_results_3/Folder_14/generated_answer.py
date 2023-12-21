
def if_contains_anagrams(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(set(lst[i].lower()) - set(lst[j].lower())) == 0 and len(set(lst[j].lower()) - set(lst[i].lower())) == 0 and len(lst[i]) >= 3 and len(lst[j]) >= 3:
                counter += 1
                if counter > 474:
                    return False
    return True
