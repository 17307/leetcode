"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/36/
"""
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_d = {}
        t_d = {}
        for i in s:
            s_d[i] = s_d.get(i, 0) + 1
        for i in t:
            t_d[i] = t_d.get(i, 0) + 1
        return s_d == t_d

    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(ord('a'), ord('z') + 1):
            if s.count(chr(i)) != t.count(chr(i)):
                return False
        return True

    def isAnagram3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        return Counter(s) == Counter(t)

    def isAnagram4(self, s, t):
        from itertools import permutations
        s_per = [''.join(i) for i in permutations(s)]
        if t in s_per:
            return True
        return False

if __name__ == "__main__":
    from itertools import permutations
    s = "tcat"
    s_per = [''.join(i) for i in permutations(s)]
    print(s_per)
    t = permutations(s)
