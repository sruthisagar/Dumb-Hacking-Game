#Hacking Game Version 4
#The game opens a window named Hacking.
#A list of passwords is diplayed green on black background and the player inputs a guess 
#Multiple attempts are allowed (atmost 4) 
#The window is cleared and the password is displayed. 
#The game gives a success outcome if the guess is correct (HUNTING) and a failure outcome otherwise.
#Repeating code is replaced by loops

from uagame import Window
from time import sleep

#create window

window=Window('Hacking', 600, 500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')
text_height=window.get_font_height()
sleep_time=0.3
attempt_no=4

#display header 

line_x=0
line_y=0
header_list=['DEBUG MODE',str(attempt_no)+' ATTEMPT(S) LEFT','']

for header in header_list :
	window.draw_string(header, line_x, line_y)
	window.update()
	sleep(sleep_time)
	line_y=line_y+text_height

#display password list

password_list=['PROVIDE','SETTING','CANTINA','CUTTING','HUNTERS','SURVIVE','HEARING','HUNTING','REALIZE','NOTHING','OVERLAP','FINDING','PUTTING','']

for password in password_list :
	window.draw_string(password, line_x, line_y)
	window.update()
	sleep(sleep_time)
	line_y=line_y+text_height

#choose password

password=password_list[7]

warning='*** LOCKOUT WARNING ***'
guess=''

while(attempt_no!=0 and guess!=password) :

	#prompt for a password

	guess=window.input_string('ENTER PASSWORD >', line_x, line_y)
	line_y=line_y+text_height
	attempt_no=attempt_no-1

	#display lockout warning

	if attempt_no==1 :
		warning_x=window.get_width()-window.get_string_width(warning)
		warning_y=window.get_height()-text_height
		window.draw_string(warning, warning_x, warning_y)

	#display attempts left

	window.draw_string(str(attempt_no), line_x, text_height)
	window.update()

#clear window

window.clear()

#create outcome

	#create success

if guess==password :
	outcome_list=[guess,'EXITING DEBUG MODE','LOGIN SUCCESSFUL - WELCOME BACK']
	prompt='PRESS ENTER TO CONTINUE'

	#create failure

else :
	outcome_list=[guess,'LOGIN FAILURE - TERMINAL LOCKED','PLEASE CONTACT AN ADMINISTRATOR']
	prompt='PRESS ENTER TO EXIT'

#display outcome

outcome_height=7*text_height
line_y=(window.get_height()-outcome_height)/2

for outcome in outcome_list :
	line_x=(window.get_width()-window.get_string_width(outcome))/2

	window.draw_string(outcome, line_x, line_y)
	window.update()
	sleep(sleep_time)

	line_y=line_y+2*text_height

#prompt for end

line_x=(window.get_width()-window.get_string_width(prompt))/2
window.input_string(prompt, line_x, line_y)

#close window

window.close()