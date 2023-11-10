def romanToInt(s: str) -> int: # my solution 
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    n = len(s)

    res = 0
    skip = False

    for ind in range(n):
        if skip: 
            skip = False
            continue
        if ind != n-1 and roman[s[ind]] < roman[s[ind+1]]:
            res += (roman[s[ind+1]] - roman[s[ind]])
            skip = True
        else: 
            res += roman[s[ind]]

    return res

def romanToInt2(s: str) -> int: # top solutions
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


s = ["III", "LVIII", "MCMXCIV"]


print(romanToInt(s[1]))
