class Solution:
    
    def romanToInt(self, s: str) -> int:
        
        values = []

        conversions = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000
        }

        # Handle special cases of 4,9,40,90,400,500, and 900 first
        for numeral in [char for char in conversions.keys() if len(char) > 1]:

            if numeral in s:
                
                s = s.replace(numeral, "")
                values.append(conversions[numeral])

        for numeral in [char for char in s]:

            values.append(conversions[numeral])

        return sum(values)

if __name__ == '__main__':
    
    solution = Solution()

    print(solution.romanToInt("MCMXCIV"))