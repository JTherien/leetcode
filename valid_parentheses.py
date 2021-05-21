class Solution:
    
    def isValid(self, s: str) -> bool:
        
        ls = [char for char in s]
        
        opposite = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        if len(ls) % 2 == 0:

            paren_stack = []
  
            for char in ls:

                if char in ['(', '[', '{']:

                    paren_stack.append(char)

                elif len(paren_stack) == 0:

                    return False

                elif paren_stack.pop() != opposite[char]:

                    return False

            if len(paren_stack) == 0:

                return True

            else:

                return False

        else:

            return False

if __name__ == '__main__':
    
    solution = Solution()

    print(solution.isValid("(("))