import collections
def if_contains_anagrams(input_list):
    result = False
    for x in input_list:
        for y in input_list:
            if len(x)>=3 and len(y)>=3 and x!=y:
                if sorted(x.lower())==sorted(y.lower()):
                    result = True
                    break
    return result
