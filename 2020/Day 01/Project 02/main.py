inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()
inputNumbers = []

for inputs in inputLines:
  inputNumbers.append(inputs.strip())

#print(inputNumbers)

answer = 0

for inputOne in inputNumbers:
  for inputTwo in inputNumbers:
    for inputThree in inputNumbers:
      #print("Inputs: ", inputOne, inputTwo)
      if (int(inputOne) + int(inputTwo) + int(inputThree) == 2020):
        answer = int(inputOne) * int(inputTwo) * int(inputThree)
        break
    if answer > 0:
      break
  if answer > 0:
    break

print(inputOne, inputTwo, inputThree, answer)