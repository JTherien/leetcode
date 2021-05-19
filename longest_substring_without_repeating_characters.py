class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0

        for i in range(len(s)):

            if result >= (len(s) - i):

                return result

            for j in range(i + result,len(s)+1):
                
                if len(s[i:j]) == len(''.join(set(s[i:j]))):

                    result = max(len(s[i:j]), result)

                else:

                    break

        return result
    