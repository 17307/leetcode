import math


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        flag_new = None
        flag_num = 1
        num = 0
        for i in str:
            if flag_new:
                if '0' <= i <= '9':
                    num = num * 10 + int(i)
                else:
                    if num:
                        break
                    else:
                        return 0
            else:
                if i == " ":
                    continue
                elif i == '+':
                    flag_new = True
                    continue
                elif i == '-':
                    flag_new = True
                    flag_num = 0
                elif '0' <= i <= '9':
                    flag_new = True
                    num = num * 10 + int(i)
                else:
                    return 0
        if flag_num == 0:
            num = -num
            if num < math.pow(2, 31) * -1:
                num = math.pow(2, 31) * -1
        else:
            if num > math.pow(2, 31) - 1:
                num = math.pow(2, 31) - 1

        return int(format(num, ".0f"))


if __name__ == "__main__":
    s = Solution()
    n = s.myAtoi("as sa 1d12")
    print(n)
