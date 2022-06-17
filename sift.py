import time

class Card:
    # Constructor for initializing a card from input
    # Extracts 4 attributes - color, symbol, shade and number from the input line
    def __init__(self, cardRep):
        cardRepList = cardRep.split(' ')
        color, symbols = cardRepList[0], cardRepList[1]
        self.rep = cardRep
        if symbols[0] in ['a', 's', 'h']:
            shading = 'lower'
            symbol = symbols[0]
        elif symbols[0] in ['A', 'S', 'H']:
            shading = 'upper'
            symbol = symbols[0].lower()
        else:
            shading = 'special'
            if symbols[0] == '@':
                symbol = 'a'
            elif symbols[0] == '$':
                symbol = 's'
            else:
                symbol = 'h'
        number = len(symbols)
        self.attributes = [color, symbol, shading, number]

    # Given two cards, will return a boolean representing whether current card with second and third card forms a set.
    def isSet(self, secondCard, thirdCard):
        def sameAttributes(att1, att2, att3):
            return att1 == att2 and att2 == att3

        def differentAttributes(att1, att2, att3):
            return len({att1, att2, att3}) == 3

        return all(sameAttributes(att1, att2, att3) or differentAttributes(att1, att2, att3)
                   for (att1, att2, att3) in zip(self.attributes, secondCard.attributes, thirdCard.attributes))

    # Overriding tostring()
    def __str__(self):
        return self.rep

    def __repr__(self):
        return str(self.rep)


# Dynamic programming based solution for finding collections of disjoint set
def dpLargestDisjoint(set_of_cards, setList=None, memo=None):
    if setList is None:
        setList = set()
    if memo is None:
        memo = []
    if memo:
        yield memo
    for i, x in enumerate(set_of_cards):
        if setList.isdisjoint(x):
            for card in dpLargestDisjoint(set_of_cards[i + 1:], setList | set(x), memo + [x]):
                yield card

# Utility to find the largest collection of disjoint set
def dpLargestDisjointSetUtil(cards):
    largest_disjoint_set = []
    for result in dpLargestDisjoint(cards):
        if len(result) > len(largest_disjoint_set):
            largest_disjoint_set = result
    return largest_disjoint_set

# Following functions isDisjoint(), recursiveDisjointSetsUtil() and recursiveDisjointSets() implements a naive approach to find largest collection
# of disjoint sets.

# A utility function to determine whether set2 forms a disjoint set collection with a set of cards.
def isDisjoint(setOfSets, set2):
    cardMap = {}
    for set1 in setOfSets:
        for card in set1:
            cardMap[card.rep] = 1

    for card in set2:
        if card.rep in cardMap:
            return False

    return True

# Recursive utility for finding disjoint sets
def recursiveDisjointSetsUtil(sets, start, end, disjointSets):
    if start >= end:
        return disjointSets
    if isDisjoint(disjointSets, sets[start]):
        inclusive = recursiveDisjointSetsUtil(sets, start + 1, end, disjointSets + [sets[start]])
        exclusive = recursiveDisjointSetsUtil(sets, start + 1, end, disjointSets)
        return inclusive if len(inclusive) > len(exclusive) else exclusive
    return recursiveDisjointSetsUtil(sets, start + 1, end, disjointSets)

# Recursive solution to find largest disjoint sets
def recursiveDisjointSets(sets):
    return recursiveDisjointSetsUtil(sets, 0, len(sets), [])


if __name__ == '__main__':

    # read first line of input - number of cards
    n = int(input())

    # Based on number of cards, read n lines representing n cards (as card objects) and persist in a list
    cards = []
    for i in range(n):
        line = input()
        cards.append(Card(line))

    # sets will contain the sets of card
    sets = []

    # Go through all combinations of cards and find the sets of card/
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            for k in range(j + 1, len(cards)):
                if cards[i].isSet(cards[j], cards[k]):
                    sets.append((cards[i], cards[j], cards[k]))

    # output the number of sets found
    n = len(sets)
    print(n)

    # calculate largest collection of disjoint sets
    disjointSets = dpLargestDisjointSetUtil(sets)

    # output the number of sets in the largest collection of disjoint sets
    print(len(disjointSets))
    print()

    # Output the cards in each set present in the largest collection of disjoint sets.
    for disjointSet in disjointSets:
        for card in disjointSet:
            print(card)
        print()