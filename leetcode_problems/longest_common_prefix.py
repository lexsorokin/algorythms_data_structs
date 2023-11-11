def longestCommonPrefix(strs: list[str]) -> str:

    common_prefix = ""

    sorted_strs = sorted(strs) #sort array lexicographically

    first_str = sorted_strs[0]
    last_str = sorted_strs[-1]

    for i in range(min(len(first_str), len(last_str))): # iterating until the length of the min char
        if first_str[i] != last_str[i]:
            return common_prefix
        common_prefix += first_str[i]

    return common_prefix

    
        #         ans=""
        # v=sorted(v)
        # first=v[0]
        # last=v[-1]
        # for i in range(min(len(first),len(last))):
        #     if(first[i]!=last[i]):
        #         return ans
        #     ans+=first[i]
        # return ans 
        

        


s = ["flower","flow","flight"]
s2 = ["dog","racecar","car"]
s3 = ["flower"]
s4 = ["a"]

s5 = ["a","asdfa","flower"]
s6 = ["ab", "a"]

a = [s, s2, s3, s4, s5, s6]
for i in a: 
    print(longestCommonPrefix(i))

# print(longestCommonPrefix(s6))
