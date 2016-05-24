'''
Reads through files and parses out paragraphs (denoted by newline characters)
'''

f = open('workfile', 'r')

text = []

while(line is not ""):
  line = f.readLine()
  if line is not "\n":
    text += [line[:len(line)-2]] #-2 is to remove \n from line end

print(text)
