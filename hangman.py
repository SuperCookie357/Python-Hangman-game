# HANGMAN code by Simon Scurtu 2024 Copyright All rights reserved bladhy bladhy blah yhady yadha yadha
from random import *
from time import sleep,time
import os

#Here i check operating system type ie: windows / linux / mac os
system_name = os.name
if system_name == "nt":           #windows uses "cls" to clear terminal output 
        clear_command = "cls"
else:
        clear_command = "clear"   # apple and linux both use "clear" to clear terminal output dont ask me why windows has to be different idk why XD

lines = "===================================================================================================================================================================================================================================="

banner = """
                                	                                                        ____          ____          ____
											|    | |    | |\\   | |      |\\  /| |    | |\\   |
											|____| |____| | \\  | |  __  | \\/ | |____| | \\  |
											|    | |    | |  \\ | |	  | |    | |    | |  \\ |
											|    | |    | |   \\| |____| |    | |    | |   \\|
                                                                                                                      created by Simon Scurtu 2024
"""

end_banner = """
										 _____   ____          _____        _____            _____   ____
										|	|    | |\\  /| |            |     | |      | |       |    |   |
										|   ___ |____| | \\/ | |____        |     |  \\    /  |___    |___/    |
										|     | |    | |    | |            |     |   |  |   |       |   \\    |
										|_____| |    | |    | |_____       |_____|    \\/    |_____  |    |   O
"""

win_banner = """
												      _____
											       |   | |     | |     |     |       | | |\\    | |
												\\ /  |     | |     |     |   |   | | | \\   | |
												 |   |     | |     |      | | | |  | |   \\ | |
												 |   |_____| |_____|       |   |   | |    \\| O
"""
stage1 = """
													__________________
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
												_______	|________________________________________
"""
stage2 = """
													__________________
													|               |
													|		|
													|		|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
												_______	|________________________________________
"""
stage3 = """
													__________________
													|		|
													|		|
													|	       _|_
													|	      |   |
													|	      |_ _|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
													|
												_______	|________________________________________
"""
stage4 = """
													__________________
													|		|
													|		|
													|	       _|_
													|	      |   |
													|	      |_ _|
													|	       	|
													|	        |
													|	        |
													|               |
													|		|
													|
													|
													|
													|
													|
													|
													|
												_______	|________________________________________
"""
stage5 = """
													__________________
													|		|
													|		|
													|	       _|_
													|	      |   |
													|	      |_ _|
													|	       /|\\
													|	     /  |  \\
													|	   /	|    \\
													|     	 	|
													|	        |
													|
													|
													|
													|
													|
													|
													|
												________|________________________________________
"""
stage6 =  """
													__________________
                                                                                                        |		|
													|		|
													|	       _|_
													|             |x x|
													|             |_ _|
													|              /|\\
													|	     /	|  \\
													|	   /	|    \\
													|		|
													|		|
													|              / \\
													|            /     \\
													|          /         \\
													|
													|
													|
													|
												_______	|________________________________________
"""
stages = [stage1,stage2,stage3,stage4,stage5,stage6]

#feel free to add more words or even change the words i used to add more difficult words
words = ["parrot","flamingo","telephone","gramophone","sausage","gorgonzola","mozzarella","ridiculous","junction","geometry","butcher","butter","video","raspberry","lighter","flower","grass","computer","juice","knife","hospital",\
"banana","potato","tomato","sauce","broccoli","asparagus","cauliflower","coal","bicycle","garage","elevator","temple","horizon","capture","serpent","galaxy","lantern","mirage","eclipse","riddle","cascade","velvet","avalanche", \
"apple","moon","water","bread","rope","light","photograph","cloud","horse","house","room","nose","coin","milk","song","goat","puzzle","basket","picnic","market","thunder","rocket","compass","volcano","guitar","glider","castle"]


global current_stage
current_stage = ""

global prompt
prompt = ""

global letters_remaining 
letters_remaining = 100

def setup():
	global current_stage
	os.system(clear_command)
	current_word = " "
	found_letters = []
	draw_title()
	current_stage = 0
	draw_stage(stages[current_stage])

def draw_stage(stage):
	print(stage)
	print()
def draw_title():
	print(lines)
	print(banner)
	print(lines)

def draw_dashes(n):
	print("                                                                                                                ", end=" ")
	for i in range(n):
		print("_", end=" ")
	print()
def redraw_dashes():
	os.system(clear_command)
	draw_title()
	draw_stage(stages[current_stage])
	print("                                                                                                                ", end=" ")
	for l in word:
		if l in found_letters:
			print(l, end=" ")
		else:
			print("_", end=" ")
	print()

def count_indiv_letter(string):
	char_list = list(set(string))
	return char_list

def refresh(stage):
	os.system(clear_command)
	draw_title()
	draw_man(stage)
	draw_dashes(len(current_word))

def pick_word():
	global word
	global letters_remaining
	global indiv_letters

	word = choice(words)
	indiv_letters = count_indiv_letter(word)
	letters_remaining = len(indiv_letters)
	letter_list = list()
	for letter in range(len(word)):
		l = word[letter]
		letter_list.append(l)
	draw_dashes(len(word))
	return letter_list

def game_over():
	print(end_banner)

def win():
	print(win_banner)

#MAIN LOOP
while True:
        setup()
        letter_list = pick_word()
        found_letters = []
        wrong_letters = []
        solving_word = True
        while solving_word:
                if letters_remaining == 0:
                        win()
                        iswin = True
                        print(iswin)
                        solving_word = False
                        break
                else:
                        print()
                        print()
                        print("                        	        	                                                                  Pick a letter")
                        prompt = str(input("                                                                                                                        "))
                        prompt.lower()
        
                        if len(prompt) == 1:
                                if prompt in letter_list and prompt not in found_letters:
                                        for l in range(len(prompt)):
                                                found_letters.append(prompt[l])
                                        redraw_dashes()
                                        letters_remaining -= 1
                                elif prompt in letter_list and prompt in found_letters:
                                	print()
                                	print()
                                	print("                                                                                                         Letter already found, try another")
                                	sleep(2)
                                	os.system(clear_command)
                                	draw_title()
                                	draw_stage(stages[current_stage])
                                	redraw_dashes()
                                elif prompt not in letter_list and stages[current_stage] != stage5:
                                	wrong_letters.append(prompt)
                                	os.system(clear_command)
                                	draw_title()
                                	current_stage += 1
                                	draw_stage(stages[current_stage])
                                	if len(found_letters) == 0:
                                		draw_dashes(len(word))
                                	else:
                                		redraw_dashes()
                                elif prompt not in letter_list and stages[current_stage] == stage5:
                                	os.system(clear_command)
                                	draw_title()
                                	current_stage += 1
                                	draw_stage(stages[current_stage])
                                	solving_word = False
                                	iswin = False
                                	print(iswin)
                                	game_over()
                                	break
                        else:
                        	print()
                        	print()
                        	print("                                                                                                             Only 1 letter at a time!")
                        	sleep(3)
                        	os.system(clear_command)
                        	draw_title()
                        	draw_stage(stages[current_stage])
                        	if len(found_letters) == 0:
                        		draw_dashes(len(word))
                        	else:
                        		redraw_dashes()
        break

if iswin == True:
        pattern = "YOU WIN!     "
elif iswin == False:
        pattern = "YOU LOSE!     "
for i in range(1000):
        print(pattern, end=" ")
        sleep(0.1)

input()
