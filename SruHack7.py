#Hacking Game Version 4
#The game opens a window named Hacking.
#A list of passwords is diplayed green on black background and the player inputs a guess 
#Multiple attempts are allowed (atmost 4) 
#The window is cleared and the password is displayed. 
#The game gives a success outcome if the guess is correct (HUNTING) and a failure outcome otherwise.
#Repeating code is replaced by loops
#Functions are used to avoid repeating code by mutiple calls
#Each passwrd is embedded with 13 random symbols

from uagame import Window
from time import sleep
from random import randint, choice

hint_y=0

def main():

	location=[0,0]
	window=create_window()
	attempt_no=4
	password_list=['PROVIDE','SETTING','CANTINA','CUTTING','HUNTERS','SURVIVE','HEARING','HUNTING','REALIZE','NOTHING','OVERLAP','FINDING','PUTTING']
	password=password_list[7]
	no_of_symbols=13

	display_header(window, attempt_no, location)
	location=display_password_list(window, password_list, no_of_symbols, location)
	guess=get_guesses(window, attempt_no, password, location)
	end_game(window, guess, password, location)

def create_window():

	window=Window('Hacking', 600, 500)
	window.set_font_name('couriernew')
	window.set_font_size(18)
	window.set_font_color('green')
	window.set_bg_color('black')
	return window
	
def display_header(window, attempt_no, location):

	header_list=['DEBUG MODE',str(attempt_no)+' ATTEMPT(S) LEFT','']

	for header in header_list :
		display_line(window, header, location)

def display_line(window, string, location):

		sleep_time=0.3
		text_height=window.get_font_height()
		window.draw_string(string, location[0], location[1])
		window.update()
		sleep(sleep_time)
		location[1]=location[1]+text_height

def display_password_list(window, password_list, no_of_symbols, location):

	for password in password_list :
		embedding=embed_password(password, no_of_symbols)
		display_line(window, embedding, location)

	location[1]=location[1]+window.get_font_height()
	return location


def embed_password(password, no_of_symbols):

	fill='!@#$%^&*()-+=~[]{}'
	embedding=''
	password_size=len(password)
	split_index=randint(0, no_of_symbols-password_size)

	for index in range(0, split_index):
		embedding=embedding+choice(fill)

	embedding=embedding+password

	for index in range(split_index+password_size, 20):
		embedding=embedding+choice(fill)

	return embedding

def get_guesses(window, attempt_no, password, location):
	
	guess=''

	while(attempt_no!=0 and guess!=password) :

		if attempt_no<4:
			display_hint(window, guess, password)

		#prompt for a password

		guess=prompt_user(window, 'ENTER PASSWORD >', location)
		location[1]=location[1]+window.get_font_height()
		attempt_no=attempt_no-1

		#display lockout warning

		check_warning(window, attempt_no)		

		#display attempts left

		window.draw_string(str(attempt_no), location[0], window.get_font_height())
		window.update()

	return guess

def prompt_user(window, prompt, location):

	capture=window.input_string(prompt, location[0], location[1])
	return capture

def check_warning(window, attempt_no):

	warning='*** LOCKOUT WARNING ***'

	if attempt_no==1 :
		warning_x=window.get_width()-window.get_string_width(warning)
		warning_y=window.get_height()-window.get_font_height()
		window.draw_string(warning, warning_x, warning_y)

def display_hint(window, guess, password):

	global hint_y
	hint_x=window.get_width()//2
	window.draw_string(guess+' INCORRECT', hint_x, hint_y)
	window.update()
	sleep(0.3)
	hint_y=hint_y+window.get_font_height()

	count=0
	for i,letter in enumerate(password):
		if i<len(guess):
			if letter==guess[i]:
				count=count+1
		else:
			break

	window.draw_string(str(count)+'/'+str(len(password))+' IN MATCHING POSITIONS', hint_x, hint_y)
	window.update()
	sleep(0.3)
	hint_y=hint_y+window.get_font_height()

def end_game(window, guess, password, location):

	#clear window

	window.clear()

	#create success

	if guess==password :
		outcome_list=[guess,'EXITING DEBUG MODE','LOGIN SUCCESSFUL - WELCOME BACK']
		prompt='PRESS ENTER TO CONTINUE'

		#create failure

	else :
		outcome_list=[guess,'LOGIN FAILURE - TERMINAL LOCKED','PLEASE CONTACT AN ADMINISTRATOR']
		prompt='PRESS ENTER TO EXIT'

	display_outcome(window, outcome_list, prompt, location)

	#close window

	window.close()

def display_outcome(window, outcome_list, prompt, location):

	outcome_height=7*window.get_font_height()
	location[1]=(window.get_height()-outcome_height)/2

	for outcome in outcome_list :

		location[0]=(window.get_width()-window.get_string_width(outcome))/2
		display_line(window, outcome, location)
		location[1]=location[1]+window.get_font_height()

	location[0]=(window.get_width()-window.get_string_width(prompt))/2
	prompt_user(window, prompt, location)

main()
