
def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            lowercase_string = string.lower()
            sorted_string = "".join(sorted(lowercase_string))
            anagrams.append((sorted_string, string))
    
    pairs = []
    for i in range(len(anagrams)):
        for j in range(i+1, len(anagrams)):
            if anagrams[i][0] == anagrams[j][0]:
                pairs.append((anagrams[i], anagrams[j]))
    
    return len(pairs) <= 41
