import math


class Solution:
    def reverse(self, x: int):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
        n = 0
        flag = False
        if x < 0:
            x = abs(x)
            flag = True
        while x != 0:
            n = n * 10 + x % 10
            x = x // 10
        if n > (math.pow(2, 31) - 1) or n < (-math.pow(2, 31)):
            return 0
        if flag:
            return -n
        else:
            return n


if __name__ == "__main__":
    s = Solution()
    n = 1534236469
    n = s.reverse(n)
    print(n)
    # print()
