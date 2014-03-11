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
    ranks.sort(reverse=True)   
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
    return ranks

# Input: a list of card ranks, example: [10,9,8,7,6]
# Output: True if ranks form a straight hand, false otherwise
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    prev = ranks[0]+1
    for rank in ranks:
        if (prev - rank) is not 1:
            return False
        prev = rank
    return True
    
# Input: a list of cards in a hand, example: ['6C','9C','8C','7C','6C']
# Output: True if the hand form a flush hand, false otherwise
def flush(hand):
    "Return True if all the cards have the same suit."
    prev = hand[0][1]
    for r,h in hand:
        if h != prev:
            return False
        prev = h
    return True
    
# Input:
# n -> the hand has exactly n of
# ranks -> a list of card ranks
# Output:
# if the hand is "9D 9H 9S 9C 7D"
# ranks -> [9,9,9,9,7]
# if we call kind(4,ranks), it should return 9,
# because the hand has 4 of 9
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    if not ranks:
        return None
    count = {}
    for rank in ranks:
        if rank in count:
            count[rank] = count[rank] + 1
        else:
            count[rank] = 1
    for k,v in count.items():
        if v == n:
            return k
    return None    

# Input: a list of card ranks, example: [10,9,8,7,6]
# Output: returns a tuple of the two ranks (high,low), None otherwise
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    count = {}
    tp_rank = []
    for r in ranks:
        if r in count:
            count[r] += 1
        else:
            count[r] = 1
    for k,v in count.items():
        if v == 2:
            tp_rank.append(k)
    if len(tp_rank) == 2:
        tp_rank.sort(reverse=True)
        return tuple(tp_rank)
    return None

def test():
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "9D 9H 8S 8D KH".split() # Two Pair
    pair = ['AC', '3D', '4S', 'KH', 'KS']
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    
    assert straight(card_ranks(al)) == True 
 
    assert card_ranks(sf) == [10,9,8,7,6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]
    assert card_ranks(pair) == [14,13,13,4,3]    
    
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False

    assert two_pair(card_ranks(tp)) == (9,8)
    assert two_pair(card_ranks(pair)) == None

    fkranks = card_ranks(fk)
     
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    
    print 'Test Passed'
    return True

test()
