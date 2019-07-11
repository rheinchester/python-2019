# My implentation o monte carlo simulation
import random
def noReplacementSimulation(numTrials):
    '''
    Author: Jacob Okoro
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    allRed = 0
    for i in range(numTrials):
        picks = pickFromBucket(3)
        if picks == 1:
            allRed +=1
    return allRed/numTrials 

def pickFromBucket(picks):
    pickList = ['red', 'green', 'red', 'green', 'red', 'green']
    picked = []
    for i in range(3):
        ball = pickList.pop(pickList.index(random.choice(pickList)))
        picked.append(ball)
    if picked[0] ==  picked[1] ==  picked[2] :
        return 1
    else:
        return 0





print(noReplacementSimulation(50000))









""" Moral of the story is:to do a monte-carlo simulaiton, all you need do is use a large to
 simulate real life events, not mathematicla events """