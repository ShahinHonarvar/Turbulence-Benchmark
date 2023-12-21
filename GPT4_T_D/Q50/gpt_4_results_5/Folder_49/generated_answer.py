
def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    
    for value in anagram_dict.values():
        if len(value) > 1:
            count += len(value)*(len(value)-1)//2
        if count >= 59:
            return True
    
    return False
