
def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                if anagrams[sorted_string] == 2:
                    count += 1
            else:
                anagrams[sorted_string] = 1
  
    return count <= 67
