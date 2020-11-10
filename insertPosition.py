def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
            
    if abs(target - nums[l]) <= abs(target - nums[r]):
        return l
    else:
        return r