
def if_contains_anagrams(string_list):
    pairs_count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if sorted(string_list[i].lower()) == sorted(string_list[j].lower()):
                pairs_count += 1
                if pairs_count > 46:
                    return False
    return True
