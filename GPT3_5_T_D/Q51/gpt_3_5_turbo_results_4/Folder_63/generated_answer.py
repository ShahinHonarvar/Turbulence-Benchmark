
def if_contains_anagrams(lst):
    count = 0
    sorted_strings = []
    
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        sorted_strings.append(sorted_string)
        
    for i in range(len(sorted_strings)):
        for j in range(i+1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                count += 1
            
    return count <= 423
