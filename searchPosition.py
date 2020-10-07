def searchRange(nums, target):
    l = 0
    r = len(nums) - 1
    last, first = -1, -1
    while l <= r:
        mid = (l + r) // 2     
        if nums[mid] <= target:         
            if nums[mid] == target:
                last = mid
            l = mid + 1
        else:
            r = mid - 1
    l = 0
    r = len(nums) - 1        
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            if nums[mid] == target:
                first = mid
            r = mid - 1
        else:
            l = mid + 1
            
    return[first, last]