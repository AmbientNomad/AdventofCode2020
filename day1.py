with open("./day1input.txt") as file:
    expenseReport = [int(eachEntry.rstrip()) for eachEntry in file]

part1 = {firstNum * secondNum for firstNum in expenseReport
         for secondNum in expenseReport
         if firstNum + secondNum == 2020}

part2 = {firstNum * secondNum * thirdNum for firstNum in expenseReport
         for secondNum in expenseReport
         for thirdNum in expenseReport
         if firstNum + secondNum + thirdNum == 2020}

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

# Part 1: 197451
# Part 2: 138233720
