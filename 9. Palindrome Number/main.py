class Solution:
    def isPalindrome(self, x: str) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
     
# Test case 1
# Input: 121
# Output: true
# Expected: true 


# Test case 2
# Input: -121
# Output: false
# Expected: false


# Test case 3
# Input: 10
# Output: false
# Expected: false