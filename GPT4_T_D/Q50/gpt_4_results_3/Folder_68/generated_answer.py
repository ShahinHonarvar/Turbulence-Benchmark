
def if_contains_anagrams(lst):
    words = [word.lower() for word in lst if len(word) >= 3]  
    anagrams = []
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                anagrams.append((words[i], words[j]))
    return len(anagrams) >= 9
