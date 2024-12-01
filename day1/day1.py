def partOne(left, right):
    left.sort()
    right.sort()

    total_distance = 0
    for i in range(0, len(left)):
        total_distance += abs(left[i] - right[i])
    print("Total Distance: %s" % total_distance)

def partTwo(left, right):
    similarity_score = 0
    occurences = 0
    for num in left:
        for num2 in right:
            if num == num2:
                occurences += 1
        similarity_score += occurences * num
        occurences = 0
    print("Similarity Score: %s" % similarity_score)


with open("day1/input.txt", 'r') as inp:
    txt = inp.read().split('\n')

left = []
right = []

for pair in txt:
    s = pair.split('   ')
    left.append(int(s[0]))
    right.append(int(s[1]))

partOne(left, right)
partTwo(left, right)

