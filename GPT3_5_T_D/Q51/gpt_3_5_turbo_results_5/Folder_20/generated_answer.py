
def if_contains_anagrams(string_list):
    import itertools
    import collections
    
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        counter1 = collections.Counter(s1)
        counter2 = collections.Counter(s2)
        return counter1 == counter2
    
    count = 0
    for i in range(len(string_list)-1):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and is_anagram(string_list[i], string_list[j]):
                count += 1
                if count > 131:
                    return False
    return True
