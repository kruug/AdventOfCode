inputNumbers = []

with open('input.txt') as inputFile:
  inputLines = inputFile.readlines()

for inputs in inputLines:
  inputNumbers.append(inputs.strip())

#print(inputNumbers)

answer = 0

for inputOne in inputNumbers:
  for inputTwo in inputNumbers:
    #print("Inputs: ", inputOne, inputTwo)
    if (int(inputOne) + int(inputTwo) == 2020):
      answer = int(inputOne) * int(inputTwo)
      break
  if answer > 0:
    break

print(inputOne, inputTwo, answer)