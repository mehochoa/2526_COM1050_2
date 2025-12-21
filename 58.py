class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       n=s.split()
       result= n[-1]
       return len(result)