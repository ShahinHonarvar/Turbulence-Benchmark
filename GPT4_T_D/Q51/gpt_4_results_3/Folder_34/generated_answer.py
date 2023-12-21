
def if_contains_anagrams(lst):
    from collections import Counter

    anagrams = []
    for word in lst:
        word_lower = word.lower()  
        if len(word_lower) >= 3:
            anagrams.append(''.join(sorted(word_lower)))  
    
    count = Counter(anagrams)
    sum_pairs = sum((i*(i-1))//2 for i in count.values())  
    
    return sum_pairs <= 401
