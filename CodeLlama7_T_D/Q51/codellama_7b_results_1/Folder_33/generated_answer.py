
def if_contains_anagrams(words):
    count = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            first = words[i].lower()
            second = words[j].lower()
            if sorted(first) == sorted(second):
                count += 1
                
    return count <= 85
