
def all_left_right_truncatable_prime(test_nums):
    res = []
    for num in test_nums:
        if num <= 945:
            current = str(num)
            while len(current) > 1:
                if current[0] == "9":
                    break
                elif current[0] == "0":
                    return []
                elif current[-1] == "0":
                    return []
                elif current[-1] == "5":
                    if len(current) > 2 and current[1] != "0":
                        break
                    else:
                        return []
                elif current[-1] == "5" or current[-1] == "0":
                    break
                elif current[-1] == "1":
                    if len(current) == 2:
                        break
                    else:
                        return []
                elif current[-1] == "2":
                    if len(current) == 3 and current[1] == "0":
                        break
                    else:
                        return []
                elif current[-1] == "3":
                    if len(current) == 2:
                        break
                    else:
                        return []
                elif current[-1] == "4":
                    if len(current) == 2:
                        break
                    else:
                        return []
                elif current[-1] == "6":
                    if len(current) == 3 and current[1] == "0":
                        break
                    else:
                        return []
                elif current[-1] == "7":
                    if len(current) == 2:
                        break
                    else:
                        return []
                elif current[-1] == "8":
                    if len(current) == 3 and current[1] == "0":
                        break
                    else:
                        return []
                elif current[-1] == "9":
                    if len(current) == 2:
                        break
                    else:
                        return []
                elif current[-1] == "2" and len(current) == 3 and current[1] == "0":
                    break
                elif current[-1] == "2" or current[-1] == "4":
                    break
                elif current[-1] == "3" or current[-1] == "5":
                    break
                elif current[-1] == "1" or current[-1] == "7":
                    break
                elif current[-1] == "0" or current[-1] == "6":
                    break
                elif current[-1] == "8":
                    if len(current) == 2:
                        break
                    else:
                        return []
                elif current[-1] == "9" or current[-1] == "2":
                    break
                elif current[-1] == "3" or current[-1] == "4":
                    break
                elif current[-1] == "5" or current[-1] == "6":
                    break
                elif current[-1] == "7" or current[-1] == "8":
                    break
                elif current[-1] == "0" or current[-1] == "1":
                    break
                elif current[-1] == "2" or current[-1] == "3":
                    break
                elif current[-1] == "4" or current[-1] == "5":
                    break
                elif current[-1] == "6" or current[-1] == "7":
                    break
                elif current[-1] == "8" or current[-1] == "9":
                    break
        if len(res) > 0:
            res.sort()
        else:
            res.append(0)
        return res
