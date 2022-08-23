def lastWord(splitted:list):
  start = splitted[0]
  for string in splitted:
    if string != '':
      start = string
  return start


def lengthOfLastWord(s: str) -> int:
        splitted  = s.split(' ')
        start = splitted[0]
        for i in range(len(splitted)-1,-1,-1):
            if splitted[i] != '':
                start = splitted[i]
                break
        return len(start)

s = "   fly me   to   the moon  "
splitted  = str.split(' ')

print(lengthOfLastWord(s))
