class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=[]
        for i in s:
            if 'a'<=i<='z':
                result.append(i)
            elif 'A'<=i<='Z':
                a=i.lower()
                result.append(a)
            elif '0'<=i<='9':
                result.append(i)
        if result==result[::-1]:
            return True
        else:
            return False