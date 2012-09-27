
def getDice():
    strDice = raw_input().split()
    return sorted(map(int,strDice))

def diff(d):
    return [d[x+1]-d[x] for x in range(len(d)-1)]

def main():
    s = 0
    sPrev = 0

    for i in range(6):
        dice = getDice()
        s += sum(x for x in dice if x == i+1)
        print s-sPrev
        sPrev = s

    #one pair
    #sum of all dice in the pair
    #dice = getDice()
    #s += max(x for x in dice if dice.count(x) > 1)*2

    #two pair
    #sum of all dice in the pair (must be two different pairs
    #and not a 4 of a kind)
    #dice = getDice()
    #pairs = {x for x in dice if dice.count(x) > 1}
    #if len(pairs) > 1:
        #m = max(pairs)
        #s += (m + max(pairs.remove(m)))*2

    #three of a kind
    #sum of all dice
    dice = getDice()
    s += sum(dice) if [x for x in dice if dice.count(x) > 2] else 0
    print s-sPrev
    sPrev = s

    #four of a kind
    #sum of all dice
    dice = getDice()
    s += sum(dice) if [x for x in dice if dice.count(x) > 3] else 0
    print s-sPrev
    sPrev = s

    #full house
    #25
    dice = getDice()
    s += 25 if [x for x in dice if dice.count(x) == 2] and [x for x in dice if dice.count(x) == 3] else 0
    print s-sPrev
    sPrev = s

    #small straight (4 sequential)
    #30
    dice = diff(sorted(set(getDice())))
    s += 30 if '1, 1, 1' in `dice` else 0
    print s-sPrev
    sPrev = s

    #large straight (5 sequential)
    #40
    dice = getDice()
    d = diff(dice)
    s += 40 if len(set(diff(dice))) == 1 and d[0] == 1 else 0
    print s-sPrev
    sPrev = s

    #yahtzee
    #50
    dice = getDice()
    s += 50 if dice.count(dice[0]) == 5 else 0
    print s-sPrev
    sPrev = s

    #chance
    #sum of all dice
    dice = getDice()
    s += sum(dice)
    print s-sPrev
    sPrev = s

    print ''
    print s

if __name__ == '__main__':
    main()
