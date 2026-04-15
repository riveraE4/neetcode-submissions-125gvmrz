class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left pointer starts @ the first index
        # right pointer starts at the last index
        # they start opposite directions, after each condition check, they move inward once
        # left += 1 and right -= 1

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True