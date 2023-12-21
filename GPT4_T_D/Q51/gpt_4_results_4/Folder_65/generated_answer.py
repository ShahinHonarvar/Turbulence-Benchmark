
def if_contains_anagrams(lst):
    n = len(lst)
    anagram_count = 0
    string_list = [sorted(string.lower()) for string in lst if len(string) >= 3]
    
    for i in range(n):
        for j in range(i+1, n):
            if string_list[i] == string_list[j]:
                anagram_count += 1
                if anagram_count > 72:
                    return False
    return True
