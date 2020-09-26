#Hacking Game Version 3
#The game opens a window named Hacking.
#A list of passwords is diplayed green on black background and the player inputs a guess (only 1 attempt is allowed). 
#The window is cleared and the password is displayed. 
#The game gives a success outcome if the guess is correct (HUNTING) and a failure outcome otherwise.

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

#display header

window.draw_string('DEBUG MODE', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('1 ATTEMPT(S) LEFT', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+2*text_height

#display password list

window.draw_string('PROVIDE', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('SETTING', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('CANTINA', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('CUTTING', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('HUNTERS', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('SURVIVE', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('HEARING', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('HUNTING', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('REALIZE', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('NOTHING', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('OVERLAP', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('FINDING', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+text_height

window.draw_string('PUTTING', line_x, line_y)
window.update()
sleep(0.3)
line_y=line_y+2*text_height

#prompt for a password

guess=window.input_string('ENTER PASSWORD >', line_x, line_y)

#clear window

window.clear()
sleep(0.3)

#create outcome

	#create success

if guess=='HUNTING' :
	outcome_line2='EXITING DEBUG MODE'
	outcome_line3='LOGIN SUCCESSFUL - WELCOME BACK'
	prompt='PRESS ENTER TO CONTINUE'

	#create failure

else :
	outcome_line2='LOGIN FAILURE - TERMINAL LOCKED'
	outcome_line3='PLEASE CONTACT AN ADMINISTRATOR'
	prompt='PRESS ENTER TO EXIT'


#display outcome

line_x=(window.get_width()-window.get_string_width(guess))/2
line_y=(window.get_height()-(7*text_height))/2

window.draw_string(guess, line_x, line_y)
window.update()
sleep(0.3)

line_x=(window.get_width()-window.get_string_width(outcome_line2))/2
line_y=line_y+2*text_height

window.draw_string(outcome_line2, line_x, line_y)
window.update()
sleep(0.3)

line_x=(window.get_width()-window.get_string_width(outcome_line3))/2
line_y=line_y+2*text_height

window.draw_string(outcome_line3, line_x, line_y)
window.update()
sleep(0.3)

line_x=(window.get_width()-window.get_string_width(prompt))/2
line_y=line_y+2*text_height

#prompt for end

window.input_string(prompt, line_x, line_y)

#close window

window.close()
