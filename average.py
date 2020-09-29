numberOfScores = 0
score1 = 0
score2 = 0
total = 0
average = 0.0
scoreCount = 0
numberOfScores = int(input("Please enter the number of scores you want to average: "))

#What python structure could we use to repeat the next 3 lines
while scoreCount < numberOfScores:
    score = int(input("Please enter a score: "))
    total = total + score
    scoreCount = scoreCount + 1

if scoreCount == numberOfScores :
    average = (total) / numberOfScores
    print(average)
