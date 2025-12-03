from input_loader import load_input

text = load_input("input.txt")

banks = text.split('\n')

part1 = 0
part2 = 0

for bank in banks:
    joltage = 0;
    firstBattery = 0;
    secondBattery = 0;
    joltages = [0,0,0,0,0,0,0,0,0,0,0,0] # 12 battery
    for i in range(len(bank)): #818181911112111 # 20 battery
        currBattery = int(bank[i])
        bankLeft = len(bank) - i
        startIndex = 0 if (len(joltages) - bankLeft) <= 0 else len(joltages) - bankLeft
        for j in range(startIndex, len(joltages)):
            if  currBattery > joltages[j]:
                joltages.insert(j, currBattery)
                joltages = joltages[:12]
                joltages[(j+1):] = [0] * (len(joltages) - (j+1))
                break

        if currBattery > secondBattery and i != 0:
            secondBattery = currBattery #2. 1 | 1 > 0 | 81
                                        #3. 8 | 8 > 1 | 88
                                        #7. 9 | 9 > 8 | 89
                                        #8. 1 | 1 > 0 | 91
                                        #12.2 | 2 > 1 | 92
        if currBattery > firstBattery and i != len(bank) - 1:
            firstBattery = currBattery  #1. 8 | 8 > 0 | 80
                                        #7. 9 | 9 > 8 | 90
            secondBattery = 0

        joltage = firstBattery * 10 + secondBattery
        #print(joltage)
        #print(joltages)


    part1 += joltage
    part2 += int("".join(map(str, joltages)))


print("Part1:" + str(part1))
print("Part2:" + str(part2))