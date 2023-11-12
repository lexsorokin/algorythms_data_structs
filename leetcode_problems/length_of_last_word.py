def lengthOfLastWord(s: str) -> int:
    length = s.split()
    if length:
        return len(length[-1])
    return 0


s = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy", ""]

for i in s:
    print(lengthOfLastWord(i))
