class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]
        x = str(x)
        return y == x