class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # an array of integers 'nums' must reach the 'target'
        # nums[i] + nums[j] == target and i != j
        # i.e. nums = [3,4,5,6] target = 7 ; [0] and [1] reach the target


        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
