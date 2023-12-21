
def if_contains_anagrams(strings):
    count = 0
    
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            string1 = strings[i].lower()
            string2 = strings[j].lower()
            
            if sorted(string1) == sorted(string2) and len(string1) >= 3:
                count += 1
                
                if count > 72:
                    return False
    
    return True
