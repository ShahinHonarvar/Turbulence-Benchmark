
def if_contains_anagrams(str_list):
    from collections import defaultdict

    def sort_and_lower(s):
        return ''.join(sorted(s.lower()))

    pairs = defaultdict(set)
    count = 0
    for string in str_list:
        sorted_string = sort_and_lower(string)
        if len(sorted_string) >= 3:
            if sorted_string in pairs and len(pairs[sorted_string]) > 0:
                count += 1
            pairs[sorted_string].add(string)
            if count > 2:
                return False
    return True
