
def getDice(f):
    strDice = raw_input().split()
    return map(int,strDice)

def main():
    s = 0

    dice = getDice()
    s += sum(x for x in dice if x == 1)
    dice = getDice()
    s += sum(x for x in dice if x == 2)
    dice = getDice()
    s += sum(x for x in dice if x == 3)
    dice = getDice()
    s += sum(x for x in dice if x == 4)
    dice = getDice()
    s += sum(x for x in dice if x == 5)
    dice = getDice()
    s += sum(x for x in dice if x == 6)
    if s > 62:
        s += 50

    #one pair
    #sum of all dice in the pair
    dice = getDice()
    s += max(x for x in dice if dice.count(x) > 1)*2
    
    #two pair
    #sum of all dice in the pair (must be two different pairs
    #and not a 4 of a kind)
    dice = getDice()
    pairs = {x for x in dice if dice.count(x) > 1}
    if len(pairs) > 1:
        m = max(pairs)
        s += (m + max(pairs.remove(m)))*2
    
    #three of a kind
    #sum of all dice
    dice = getDice()
    s += sum(dice) if [x for x in dice if dice.count(x) > 2] else 0
    
    #four of a kind
    #sum of all dice
    dice = getDice()
    s += sum(dice) if [x for x in dice if dice.count(x) > 3] else 0
    
    #small straight (4 sequential)
    #30
    dice = getDice()
    
    #large straight (5 sequential)
    #40
    dice = getDice()
    s += 40 if not [x for x in dice if dice.count(x) > 1] and (1 not in dice) or (6 not in dice) else 0
    
    #full house
    #25
    dice = getDice()
    s += 25 if [x for x in dice if dice.count(x) == 2] and [x for x in dice if dice.count == 3] else 0
    
    #chance
    #sum of all dice
    dice = getDice()
    s += sum(dice)
    
    #yahtzee
    #50
    dice = getDice()
    s += 50 if dice.count(dice[0]) == 5 else 0

if __name__ == '__main__':
    main()
