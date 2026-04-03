class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        # seen = set()
        # for x in nums:
        #     if x in seen:
        #         return True
        #     seen.add(x)
        # return False

        return len(set(nums)) < len(nums)