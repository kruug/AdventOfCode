# First number is minimum count
# Second number is maximum count
# Third element is the letter
def splitLine(line):
  inputsSplit = line.split()
  numbersSplit = inputsSplit[0].split('-')
  output = [numbersSplit[0], numbersSplit[1], inputsSplit[1].split(':')[0], inputsSplit[2]]
  return output

def isPasswordValid(minimum, maximum, let, password):
  letterCount = password.count(let)
  #print(letterCount, minimum, maximum)
  if ((letterCount >= int(minimum)) and (letterCount <= int(maximum))):
    result = True
  else:
    result = False
  #print(result)
  return result

minCount = 0
maxCount = 0
letter = 'a'
password = 'password'
validCount = 0

inputPasswords = []
validPasswords = []

with open('input.txt') as inputFile:
  inputLines = inputFile.readlines()

for inputs in inputLines:
  inputsSplit = splitLine(inputs)

  minCount = inputsSplit[0]
  maxCount = inputsSplit[1]
  letter = inputsSplit[2]
  password = inputsSplit[3]
  #print(minCount, maxCount, letter, password)
  result = isPasswordValid(minCount, maxCount, letter, password)

  if result:
    validCount = validCount + 1
    validPasswords.append(password)

print(validCount)
#print(validPasswords)