import set
def if_contains_anagrams(text):
    res = set.set(text).intersection(set.set(text))
    if len(res) <= 257:
        return True
    else:
        return False
