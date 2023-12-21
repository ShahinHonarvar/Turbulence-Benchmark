
def if_contains_anagrams(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()) and len(lst[i]) >= 3 and len(lst[j]) >= 3:
                counter += 1
                if counter > 40:
                    return False
    return True
