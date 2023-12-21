import collections
def if_contains_anagrams(test_list):
    result = False
    if len(test_list) > 1:
        # sort test_list in a dictionary for faster access
        test_dict = collections.defaultdict(list)
        for test in test_list:
            test_dict[test].append(test)
        for first in test_dict:
            for second in test_dict:
                if first == second:
                    continue
                elif len(first) >= 3 and len(second) >= 3:
                    first_lower = first.lower()
                    second_lower = second.lower()
                    if first_lower == second_lower:
                        result = True
                        break
    return result
