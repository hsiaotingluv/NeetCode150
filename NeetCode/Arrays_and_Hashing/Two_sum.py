class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        question: https://leetcode.com/problems/two-sum/
        answer: https://www.nileshblog.tech/2022/08/leet-code-two-sum-problem-solution-java-cpp-javascript-python/?utm_content=anc-true

        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                seen = {}
                for i, value in enumerate(nums):
                    remaining = target - nums[i]
                    
                    if remaining in seen:
                        return [i, seen[remaining]]
                        
                    seen[value] = i 
        """

        if len(nums) <= 2:
            return nums
        
        dict = {}
        for i in range(0, len(nums)):
            dict[i] = nums[i]
        
        for item in dict.items():
            print(item)
            print(type(item))

        list_of_tuple = sorted(dict.items(), key=lambda x:x[1])

        i = 0
        j = len(list_of_tuple) - 1

        while (list_of_tuple[i][1] + list_of_tuple[j][1] != target):
            if (list_of_tuple[i][1] + list_of_tuple[j][1] < target):
                i += 1
            else:
                j -= 1
        
        return [list_of_tuple[i][0], list_of_tuple[j][0]]
    
nums = [2,7,11,15]
target = 9
solution = Solution()
result = Solution.twoSum(solution, nums, target)
print(result)
