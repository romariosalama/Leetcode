class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for ch in s:
            if ch.isalnum():
                lower_ch = ch.lower()
                cleaned.append(lower_ch)

        reversed_cleaned = []
        for i in range(len(cleaned) - 1, -1, -1):
            reversed_cleaned.append(cleaned[i])

        for i in range(len(cleaned)):
            if cleaned[i] != reversed_cleaned[i]:
                return False

        return True






