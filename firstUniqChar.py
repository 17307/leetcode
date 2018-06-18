class Solution:
    def firstUniqChar(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        f = []
        while i < len(s):
            if s.rindex(s[i]) == s.index(s[i]):
                f.append(i)
            i += 1
        if not f:
            return -1
        else:
            return f[0]


if __name__ == "__main__":
    s = Solution()
    s_t = "cbc"
    print(s.firstUniqChar(s_t))
    # print(s_t.rindex(s_t[1]))
    # a = [1,2,3]