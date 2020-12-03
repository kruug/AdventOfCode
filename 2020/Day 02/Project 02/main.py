# First number is minimum count
# Second number is maximum count
# Third element is the letter
def splitLine(line):
  inputsSplit = line.split()
  numbersSplit = inputsSplit[0].split('-')
  output = [numbersSplit[0], numbersSplit[1], inputsSplit[1].split(':')[0], inputsSplit[2]]
  return output

def isPasswordValid(first, second, let, password):
  #letterCount = password.count(let)
  #print(letterCount, minimum, maximum)
  one = password.find(let, int(first), int(first)+1)
  #print(one)
  two = password.find(let, int(second), int(second)+1)
  #print(two)

  if (((int(one) >= 0) and not (int(two) >= 0)) or (not (int(one) >= 0) and (int(two) >= 0))):
    result = True
  else:
    result = False
  #print(result)
  return result

firstIndex = 0
secondIndex = 0
letter = 'a'
password = 'password'
validCount = 0

inputPasswords = []
validPasswords = []

with open('input.txt') as inputFile:
  inputLines = inputFile.readlines()

for inputs in inputLines:
  inputsSplit = splitLine(inputs)

  firstIndex = inputsSplit[0]
  secondIndex = inputsSplit[1]
  letter = inputsSplit[2]
  password = inputsSplit[3]
  #print(firstIndex, secondIndex, letter, password)
  result = isPasswordValid(int(firstIndex)-1, int(secondIndex)-1, letter, password)

  if result:
    validCount = validCount + 1
    validPasswords.append(password)

print(validCount)
#print(validPasswords)