def if_contains_anagrams(test_list):
    return sum(
        1
        for item in test_list
        for similar in test_list
        if similar.lower() == item.lower() and len(similar) >= 3
    ) >= 17
