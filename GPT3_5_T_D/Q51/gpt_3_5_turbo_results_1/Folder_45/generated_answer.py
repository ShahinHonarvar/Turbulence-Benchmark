
def if_contains_anagrams(strings):
    anagrams_count = 0
    
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()) and len(strings[i]) >= 3 and len(strings[j]) >= 3:
                anagrams_count += 1
                
    return anagrams_count <= 464
