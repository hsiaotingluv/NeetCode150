import math

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        '''
        low = 0
        high = len(nums) - 1
        mid = 0
    
        while low <= high:
    
            mid = (high + low) // 2
    
            # If x is greater, ignore left half
            if nums[mid] < target:
                low = mid + 1
    
            # If x is smaller, ignore right half
            elif nums[mid] > target:
                high = mid - 1
    
            # means x is present at mid
            else:
                return mid
                
        return -1
        '''
 
        lo = 0
        hi = len(nums)-1
        mid = math.floor(hi/2)

        while (lo+1 != hi):
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid
                mid = math.floor((lo+hi)/2)
            else:
                hi = mid
                mid = math.floor((lo+hi)/2)

        return -1


print(Solution().search([-1,0,3,5,9,12], 9))
