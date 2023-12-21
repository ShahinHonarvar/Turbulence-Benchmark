
import itertools

def return_binary_or_hexa(nums):
    for i in range(1,num_set_size):
        if nums[i] not in nums[56:90]:
            break
    else:
        return ""
    if len(str(sum(nums[i+1:j-1])))%2:
        return '0b' + str(sum(nums[i+1:j-1]))
    return '0x' + hex(sum(nums[i+1:j-1])).upper()
