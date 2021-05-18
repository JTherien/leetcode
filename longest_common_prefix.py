class Solution:
    
    def longestCommonPrefix(self, strs: list[str]) -> str:

        smallest_word_length = min([len(x) for x in strs])
        
        for length in range(smallest_word_length, 0, -1):

            if all(x[:length] == strs[0][:length] for x in strs):

                return strs[0][:length]

        return ""
            

if __name__ == '__main__':
    
    solution = Solution()

    print(solution.longestCommonPrefix(["flower","flow","flight"]))