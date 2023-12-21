def if_contains_anagrams(input_list):
    result = False
    for i in range(len(input_list) - 1):
        for j in range(i + 1, len(input_list)):
            if input_list[i].lower() == input_list[j].lower():
                continue
            elif sorted(input_list[i].lower()) == sorted(input_list[j].lower()):
                result = True
                break
    return result
