
def if_contains_anagrams(str_list):
    from collections import Counter
    
    def is_anagram(str_1, str_2):
        return Counter(str_1.lower()) == Counter(str_2.lower())

    def possible_anagrams(lst):
        count = 0 
        n = len(lst)
        for i in range(n):
            for j in range(i+1, n):
                if len(lst[i])>=3 and len(lst[j])>=3 and is_anagram(lst[i], lst[j]):
                    count += 1
                if count > 25:
                    return True
        return False

    return possible_anagrams(str_list)
