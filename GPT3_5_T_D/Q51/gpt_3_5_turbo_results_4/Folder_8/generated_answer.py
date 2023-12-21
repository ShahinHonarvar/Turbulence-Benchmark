
def if_contains_anagrams(lst):
    def get_key(string):
        return ''.join(sorted(string.lower()))

    pairs = 0
    count = {}
    for string in lst:
        if len(string) >= 3:
            key = get_key(string)
            count[key] = count.get(key, 0) + 1
            if count[key] % 2 == 0:
                pairs += 1
            if pairs > 68:
                return False
    return True
