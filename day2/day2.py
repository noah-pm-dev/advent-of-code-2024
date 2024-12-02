def checkReport(report):
    for i in range(1, len(report)):
        val = report[i]
        prev = report[i - 1]
        if (val == prev) or (abs(val - prev) not in [1, 2, 3]) or (i >= 2) and (((val - prev) * (prev - report[i - 2])) < 0):
            return 'unsafe'
    return 'safe'

def partOne(reports):
    safe_count = 0
    vals = []
    for report in reports:
        vals = [int(v) for v in report.split(' ')]

        if (checkReport(vals) == 'safe'):
            safe_count += 1
    
    print(safe_count)

def partTwo(reports):
    safe_count = 0
    vals = []
    for report in reports:
        vals = [int(v) for v in report.split(' ')]
        mocks = []
        for i in range(len(vals)):
            cp = vals.copy()
            cp.pop(i)
            mocks.append(cp)
        
        if (checkReport(vals) == 'safe'):
            safe_count += 1
        else:
            for mock in mocks:
                if checkReport(mock) == 'safe':
                    safe_count += 1
                    break
    
    print(safe_count)



with open("day2/input.txt", 'r') as inp:
    reports = inp.read().split('\n')


#partOne(reports)
partTwo(reports)

