import collections
def if_contains_anagrams(list1):
    list_of_anagrams={}
    for s in list1:
        curr_anagrams = set()
        curr_anagrams.update(s)
        if curr_anagrams not in list_of_anagrams:
            list_of_anagrams[curr_anagrams]=1
        elif list_of_anagrams[curr_anagrams] > 445:
            return False
    return True
