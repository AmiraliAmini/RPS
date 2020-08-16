# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:12:01 2020

@author: Amirali
"""
# libraries used:
import random
# this random generator defines the computers move 
randomNumber = random.randint(1, 3)
computer = randomNumber
if computer == 1 :
         computer = 'rock'
elif computer == 2:
         computer = 'paper'
elif computer == 3:
         computer = 'scissors'

# start: the player tells the game how many rounds they want the winner to have 
print('Hello \nwelcome to Amirali\'s rock paper scissors \nremember at any point you can press q and leave the game')
name = input('What\'s your name?')
print('Nice to meet you loser :)')
roundNumber = input("How many rounds do you wanna play with Mr Amini?")

    
    # These 2 variables are used for calculating results
playerwins = 0
computerwins = 0
    
     
        

         
# GAME process starts here
while playerwins < int(int(roundNumber) / 2)+1 and computerwins < int(int(roundNumber) / 2)+1 :
         player = input('What do you feel lucky with?' +" ")
         #  code below lets the player to stop playting
         if player == "q" or player == "quit":
             break
     # access code
         if player == "rock" or player == 'paper' or player=='scissors':      
             
              print (f'Amirali\'s move is: {computer}')
          
              if player == 'rock' and computer == 'scissors':
                    print(' Amirali says you WONNNNNNN ')
                    playerwins += 1
              elif player == "rock" and computer == 'paper':
                    print('OOPS you lost this time ')
                    computerwins += 1
              elif player =='paper' and computer == 'rock':
                     print('player Congrats YOU WON')
                     playerwins += 1
              elif player == 'paper' and computer == 'scissors':
                     print('HAHAHAHA You lost')
                     computerwins += 1
              elif player == 'scissors' and computer == 'paper':
                     print('YOU WONNNNNN')
                     playerwins += 1
              elif player == 'scissors' and computer == 'rock':
                     print('Amirali BEAT you LOL') 
                     computerwins += 1
                
              else :
                     print('TIE')
                     computerwins += 1
                     playerwins += 1
                
              print(f'{name}:{playerwins}    Amirali: {computerwins}')
          
         else:       
             print("That is not what I expected to hear :|")
             
             
             
             
if playerwins > computerwins :
     print('\nCongrats you  won :|')             
else:
     print('\nAmirali won once again :)')
    
     
input('Press ENTER to exist')