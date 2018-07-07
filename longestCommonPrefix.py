class Solution:
    def longestCommonPrefix(self, strs: list):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0]) + 1):
            temp = strs[0][0:i]
            for k in strs:
                if k[0:i] != temp:
                    return strs[0][0:i - 1]
            # 判断是否为最后
            if i == len(strs[0]):
                return strs[0]

        return ""


s = Solution()
z = s.longestCommonPrefix(["c", "c"])
print(z)
