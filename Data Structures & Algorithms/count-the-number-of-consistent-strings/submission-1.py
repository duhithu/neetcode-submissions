class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedArr = [False] * 26
        for c in allowed:
            allowedArr[ord(c) - ord('a')] = True

        res = len(words)
        for w in words:
            for c in w:
                if not allowedArr[ord(c) - ord('a')]:
                    res -= 1
                    break

        return res