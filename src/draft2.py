#!/usr/bin/env python

# +=========================================+
# | @author Cole Dapprich, 2018-2020 (AMDG) |
# +=========================================+

from sys import argv, exit
import csv
import re

def getRankings(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
   
    return data

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
        
def printPos(ranks, pos):
    count = 1
    for rank in ranks:
        if bool(re.match(pos + '\d{1,3}', rank['Pos'])):
            printPlayer(rank)
            count += 1
        if count > 5:
            break
    print('')

def main(argv):
    # check for correct number of arguments; exit if check fails
    if len(argv) < 2:
        exit('USAGE: python draft.py draftRankingsCSVfilePath')
        
    rankings = getRankings(argv[1])
    printNext5(rankings)
    print('Commands:\n\t[Player Name] - pick player\n\t[QB/RB/WR/TE/DST/DEF] - show next 5 players in that position\n\tall - print(names of next 5 players in rankings\n\tquit/done - exit\n')
    pick = input('Enter Pick #1, or a command (\'help\' for list of commands): ').lower()
    pickNum = 1
    
    while 'done' != pick and 'quit' != pick:
        if pick == 'wr':
            printPos(rankings, 'WR')
            printNext5(rankings)
        
        elif pick == 'rb':
            printPos(rankings, 'RB')
            printNext5(rankings)
            
        elif pick == 'te':
            printPos(rankings, 'TE')
            printNext5(rankings)
            
        elif pick == 'qb':
            printPos(rankings, 'QB')
            printNext5(rankings)
            
        elif pick == 'dst':
            printPos(rankings, 'DST')
            printNext5(rankings)
            
        elif pick == 'def':
            printPos(rankings, 'DST')
            printNext5(rankings)
            
        elif pick == 'all':
            printNext5(rankings)
            
        elif pick == 'help':
            print('Commands:\n\t[Player Name] - pick player\n\t[QB/RB/WR/TE/DST/DEF] - show next 5 players in that position\n\tall - print(names of next 5 players in rankings\n\tquit/done - exit')
            
        else: # player picked
            names = [rank['Overall'] for rank in rankings]
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