#!/usr/bin/env python

# +=========================================+
# | @author Cole Dapprich, 2018-2020 (AMDG) |
# +=========================================+

from sys import argv, exit
import csv
import re

# 0 = wr, 1 = rb, 2 = te, 3 = qb, 4 = dst/def, 5 = k TODO: make order dynamic
positionalRankings = [ [], [], [], [], [], [] ]

def getRankings(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
   
    return data
    
def getPositionalRankings(filename, posIdx):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            positionalRankings[posIdx].append(row)

def space(num):
    spaces = ''
    for i in range(num):
        spaces += ' '
        
    return spaces
    
def printPlayer(player):
    print(player['RK'], '\t', player['PLAYER NAME'], space(22 - len(player['PLAYER NAME'])), player['POS'], '\t', player['TEAM'], '\t', player['BYE WEEK'], '\t', player['BEST'], '\t', player['WORST'], '\t', player['AVG.'])
    
def printNext5(ranks):
    print('')
    print('Rank\tPlayer\t\t\tPos\tTeam\tBye\tBest\tWorst\tAvg')
    for i in range(5):
        printPlayer(ranks[i])
    print('')
        
def printPos(ranks, pos, hasPositionFiles):
    if hasPositionFiles:
        count = 1
        posIdx = 0
        
        if pos == 'RB':
            posIdx = 1
        elif pos == 'TE':
            posIdx = 2
        elif pos == 'QB':
            posIdx = 3
        elif pos == 'DST':
            posIdx = 4
        elif pos == 'K':
            posIdx = 5
        
        for rank in positionalRankings[posIdx]:
                printPlayer(rank)
                count += 1
                if count > 5:
                    break
        print('')
    else:
        count = 1
        for rank in ranks:
            if bool(re.match(pos + '\d{1,3}', rank['POS'])):
                printPlayer(rank)
                count += 1
            if count > 5:
                break
        print('')

def main(argv):
    # check for correct number of arguments; exit if check fails
    if len(argv) < 2:
        exit('USAGE: python draft.py draftRankingsCSVfilePath [positionRankingsCSVfilePath1, positionRankingsCSVfilePath2...] (order expected is wr, rb, te, qb, dst/def, k')
        
    hasPositionFiles = len(argv) < 3
    if hasPositionFiles:
        for i in range(2, len(argv)):
            getPositionalRankings(argv[i], i - 2)
        
    rankings = getRankings(argv[1])
    printNext5(rankings)
    print('Commands:\n\t[Player Name] - pick player\n\t[QB/RB/WR/TE/DST/DEF] - show next 5 players in that position\n\tall - print(names of next 5 players in rankings\n\tquit/done - exit\n')
    pick = input('Enter Pick #1, or a command (\'help\' for list of commands): ').lower()
    pickNum = 1
    
    while 'done' != pick and 'quit' != pick:
        if pick == 'wr':
            printPos(rankings, 'WR', hasPositionFiles)
            printNext5(rankings)
        
        elif pick == 'rb':
            printPos(rankings, 'RB', hasPositionFiles)
            printNext5(rankings)
            
        elif pick == 'te':
            printPos(rankings, 'TE', hasPositionFiles)
            printNext5(rankings)
            
        elif pick == 'qb':
            printPos(rankings, 'QB', hasPositionFiles)
            printNext5(rankings)
            
        elif pick == 'dst' or pick == 'def':
            printPos(rankings, 'DST', hasPositionFiles)
            printNext5(rankings)
            
        elif pick == 'kicker' or pick == 'k':
            printPos(rankings, 'K', hasPositionFiles)
            printNext5(rankings)
            
        elif pick == 'all':
            printNext5(rankings)
            
        elif pick == 'help':
            print('Commands:\n\t[Player Name] - pick player\n\t[QB/RB/WR/TE/DST/DEF] - show next 5 players in that position\n\tall - print(names of next 5 players in rankings\n\tquit/done - exit')
            
        else: # player picked
            names = [rank['PLAYER NAME'] for rank in rankings]
            for name in names:
                if name and pick in name.lower():
                    choice = input('Pick ' + name + '? (y/n/cancel): ').lower()
                    if 'y' in choice:
                        del rankings[names.index(name)]
                        pickNum += 1
                        printNext5(rankings)
                    elif 'cancel' in choice:
                        break
        
        pick = input('Enter Pick #' + str(pickNum) + ', or a command (\'help\' for list of commands): ').lower()
    
if __name__ == "__main__":
    main(argv)