import re

def partOne(mem):
    matches = re.findall(r'mul\(\d+,\d+\)', mem)
    total = 0
    for match in matches:
        nums = re.findall(r'\d+', match)
        nums = [int(num) for num in nums]
        total += nums[0] * nums[1]
    print("Total: ", total)

def partTwo(mem):
    matches = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', mem)
    total = 0
    do = True
    for match in matches:
        if match == 'don\'t()':
            do = False
            continue
        elif match == 'do()':
            do = True
            continue
        if do == True:
            nums = re.findall(r'\d+', match)
            nums = [int(num) for num in nums]
            total += nums[0] * nums[1]
    print("Total: ", total)
        


with open("day3/input.txt", 'r') as inp:
    mem = inp.read()


partOne(mem)
partTwo(mem)