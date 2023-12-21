
import itertools

def if_contains_anagrams(lst):
    letters = [c.lower() for c in 'abcdefghijklmnopqrstuvwxyz']
    pairs = 0
   
    for i in range(len(lst)):
        w1 = lst[i].lower()
        for j in range(i+1, len(lst)):
            w2 = lst[j].lower()
            if sorted(w1) == sorted(w2) and len(w1) >= 3:
                pairs += 1
           
    if pairs <= 97:
        return True
    else:
        return False
