import re

testCases = [("T",1),
             ("not T or U", 0),
             ("not (T or U)",-1),
             ("U and not U", 0),
             ("not (F and (U xor T))",1),
             ("(not T or U) and (not U or T)",0)]

logic = ["T","F","U", "not T", "not F", "not U"]

operators = ["not","and","xor","or"]



def threevl(s):
    lines = re.split(")(",case[0])
    for line in lines:

    pass

lines = []
testOutcomes = []

for case in testCases:
    line = re.split("\s",case[0])
    lines.append(line)
    print(line)
    outcome = threevl(case[0])
    testOutcomes.append((outcome,case[1],True if outcome==case[1] else False))

print(testOutcomes)