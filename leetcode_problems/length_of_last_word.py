def lengthOfLastWord(s: str) -> int:
    l = s.split()
    if l:
        return len(l[-1])
    return 0


s = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy", ""]

for i in s:
    print(lengthOfLastWord(i))
