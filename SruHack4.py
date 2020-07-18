#Hacking Game Version 4
#The game opens a window named Hacking.
#A list of passwords is diplayed green on black background and the player inputs a guess (only 1 attempt is allowed). 
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
line_x=0
line_y=0
sleep_time=0.3

#display header

header_list=['DEBUG MODE','1 ATTEMPT(S) LEFT','']

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

#prompt for a password

guess=window.input_string('ENTER PASSWORD >', line_x, line_y)

#clear window

window.clear()
sleep(sleep_time)

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
