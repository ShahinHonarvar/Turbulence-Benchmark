
def if_contains_anagrams(lst):
    def count_anagrams(string):
        count = 0
        for i in range(len(lst)):
            if sorted(string.lower()) == sorted(lst[i].lower()) and len(string) >= 3 and len(lst[i]) >= 3 and string.lower() != lst[i].lower():
                count += 1
        return count
    
    pair_count = 0
    for i in range(len(lst)):
        pair_count += count_anagrams(lst[i])
        if pair_count > 77:
            return False
    return True
