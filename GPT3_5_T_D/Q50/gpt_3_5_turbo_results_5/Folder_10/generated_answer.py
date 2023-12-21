
def if_contains_anagrams(strings):
    from collections import Counter

    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            string1 = strings[i].lower()
            string2 = strings[j].lower()
            
            if len(string1) >= 3 and len(string2) >= 3 and Counter(string1) == Counter(string2):
                count += 1
                if count >= 52:
                    return True
    
    return False
