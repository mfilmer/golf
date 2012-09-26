
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
    
    #large straight (5 sequential)
    #40
    s += 0 if [x for x in dice if dice.count(x) > 1] else 40
    
    #full house
    #25
    
    #chance
    #sum of all dice
    
    #yahtzee
    #50

if __name__ == '__main__':
    main()
