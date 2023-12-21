
def if_contains_anagrams(lst):
    def count_anagrams(word):
        anagrams = set()
        for i in range(len(word)):
            for j in range(i+1, len(word)):
                if sorted(word[i].lower()) == sorted(word[j].lower()):
                    anagrams.add((word[i].lower(), word[j].lower()))
        return len(anagrams)
    
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            count += count_anagrams(lst[i])
    
    return count <= 54
