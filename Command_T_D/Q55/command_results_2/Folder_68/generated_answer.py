def lists_with_product_equal_n(nums):
    result = []
    i = 0
    while True:
        temp = []
        while i < len(nums):
            temp.append(nums[i])
            i += 1
        if len(temp) == 0:
            break
        if temp[0] == 1 and temp[1] == 2 and temp[2] == 3:
            result.append(temp)
        elif temp[0] == 2 and temp[1] == 4:
            result.append(temp)
        elif temp[0] == 3 and temp[1] == 6:
            result.append(temp)
        elif temp[0] == 4 and temp[1] == 8:
            result.append(temp)
        elif temp[0] == 5 and temp[1] == 10:
            result.append(temp)
        elif temp[0] == 6 and temp[1] == 12:
            result.append(temp)
        elif temp[0] == 7 and temp[1] == 14:
            result.append(temp)
        elif temp[0] == 8 and temp[1] == 16:
            result.append(temp)
        elif temp[0] == 9 and temp[1] == 18:
            result.append(temp)
        elif temp[0] == 10 and temp[1] == 20:
            result.append(temp)
        elif temp[0] == 11 and temp[1] == 22:
            result.append(temp)
        elif temp[0] == 12 and temp[1] == 24:
            result.append(temp)
        elif temp[0] == 13 and temp[1] == 26:
            result.append(temp)
        elif temp[0] == 14 and temp[1] == 28:
            result.append(temp)
        elif temp[0] == 15 and temp[1] == 30:
            result.append(temp)
