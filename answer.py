class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        i = 0
        n = len(s)
        
        # Step 1: Read and ignore leading whitespace
        while i < n and s[i].isspace():
            i += 1
        
        # Step 2: Check for an optional sign
        sign = 1
        if i < n and s[i] == '+':
            i += 1
        elif i < n and s[i] == '-':
            sign = -1
            i += 1
        
        # Step 3: Convert the following digits to an integer
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Handle overflow and underflow
            if result > (MAX_INT - digit) // 10:
                return MAX_INT if sign == 1 else MIN_INT
            
            result = result * 10 + digit
            i += 1
        
        # Step 5: Apply the sign to the result
        return sign * result

            
