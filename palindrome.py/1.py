# Palindrome Number - LeetCode Problem

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        reverse = 0
        xcopy = x

        # Reverse the number
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10

        # Check if reversed number is same as original
        return reverse == xcopy


# -------------------------
# TESTING SECTION (for VS Code)
# -------------------------
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [121, -121, 10, 0, 12321, 123]

    for num in test_cases:
        result = solution.isPalindrome(num)
        print(f"{num} -> {result}")
