# Input is a hand of cards, that is a list
# of pair rank and suit string, example: ['AC', '3D', '4S', 'KH']
# Output is the numeric rank of cards sorted descending
# example: ['AC', '3D', '4S', 'KH'] should output [14, 13, 4, 3]
def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    rankdict = {'1':1,'2':2,'3':3,'4':4,'5':5,
                '6':6,'7':7,'8':8,'9':9,
                'T':10,'J':11,'Q':12,'K':13,'A':14}
    ranks = [rankdict[r] for r,s in cards]
    #alternative:
    #ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return ranks

# Input: a list of card ranks, example: [10,9,8,7,6]
# Output: True if ranks form a straight hand, false otherwise
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    prev = ranks[0]+1
    for rank in ranks:
        if (prev - rank) is not 1:
            return False
        prev = rank
    return True
    # alternative:
    # return ((max(ranks)-min(ranks)==4)&&len(set(ranks))==5)

# Input: a list of cards in a hand, example: ['6C','9C','8C','7C','6C']
# Output: True if the hand form a flush hand, false otherwise
def flush(hand):
    "Return True if all the cards have the same suit."
    # Your code here.
    prev = hand[0][1]
    for r,h in hand:
        if h != prev:
            return False
        prev = h
    return True
    # alternative
    # return len(set([s for r,s in hand]))==1   

def test():
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    pair = ['AC', '3D', '4S', 'KH', 'KS']
    
    assert card_ranks(sf) == [10,9,8,7,6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]
    assert card_ranks(pair) == [14,13,13,4,3]    
    
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    
    print 'Test Passed'
    return True

test()
