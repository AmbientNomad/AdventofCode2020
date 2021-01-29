with open("./day2input.txt") as file:
    passwords = [eachEntry.rstrip() for eachEntry in file]
validPasswords = []

for eachPassword in passwords:
    colonIndex = eachPassword.index(":")
    dashIndex = eachPassword.index("-")
    checkPassword = [letter for letter in eachPassword[colonIndex:] if letter == eachPassword[colonIndex - 1]]
    validPasswords = [validPass for validPass in checkPassword if
                      int(eachPassword[:dashIndex]) <= len(checkPassword) <= int(
                          eachPassword[dashIndex + 1:colonIndex - 1])]

print(f"Part 1: {len(validPasswords)}")

for eachPassword in passwords:
    colonIndex = eachPassword.index(":")
    dashIndex = eachPassword.index("-")
    checkPassword = "".join([passwordOnly for passwordOnly in eachPassword[colonIndex + 2:]])

    if checkPassword[int(eachPassword[:dashIndex]) - 1] != checkPassword[
        int(eachPassword[dashIndex + 1: colonIndex - 1]) - 1]:
        if checkPassword[int(eachPassword[:dashIndex]) - 1] == eachPassword[colonIndex - 1] or \
                checkPassword[int(eachPassword[dashIndex + 1: colonIndex - 1]) - 1] == eachPassword[colonIndex - 1]:
            validPasswords.append(eachPassword)

print(f"Part 2: {len(validPasswords)}")

# Part 1: 7
# Part 2: 310

