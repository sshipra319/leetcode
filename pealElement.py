def getPeak(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if ((mid == 0 or nums[mid-1] <= nums[mid]) and 
        (mid == len(nums)-1 or nums[mid+1] <= nums[mid])):
            return mid
        
        elif ((mid > 0) and (nums[mid - 1] > nums[mid])):
            r = mid - 1
    
        else:
            l = mid + 1
    
    return 0