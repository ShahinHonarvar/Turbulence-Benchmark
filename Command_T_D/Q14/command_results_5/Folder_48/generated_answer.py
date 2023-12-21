def find_second_smallest_num(nums):
    def binary_search(left, right):
        if left >= right:
            return None
        mid = (left + right) // 2
        if mid in nums and nums[mid] <= nums[left]:
            return mid
        elif nums[left] < nums[mid]:
            return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)
    return binary_search(245, 750)
