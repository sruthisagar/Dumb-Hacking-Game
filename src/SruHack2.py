#Hacking Game Version 2
#The game opens a window named Hacking.
#A list of passwords is diplayed green on black background and the player inputs a guess (only 1 attempt is allowed). 
#The window is cleared and the password is displayed. 
#The game gives a failure outcome for all the guesses (even the correct password HUNTING).

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

#display failure outcome

line_x=(window.get_width()-window.get_string_width(guess))/2
line_y=(window.get_height()-(7*text_height))/2

window.draw_string(guess, line_x, line_y)
window.update()
sleep(0.3)

line_x=(window.get_width()-window.get_string_width('LOGIN FAILURE - TERMINAL LOCKED'))/2
line_y=line_y+2*text_height

window.draw_string('LOGIN FAILURE - TERMINAL LOCKED', line_x, line_y)
window.update()
sleep(0.3)

line_x=(window.get_width()-window.get_string_width('PLEASE CONTACT AN ADMINISTRATOR'))/2
line_y=line_y+2*text_height

window.draw_string('PLEASE CONTACT AN ADMINISTRATOR', line_x, line_y)
window.update()
sleep(0.3)

line_x=(window.get_width()-window.get_string_width('PRESS ENTER TO EXIT'))/2
line_y=line_y+2*text_height

#prompt for end

window.input_string('PRESS ENTER TO EXIT', line_x, line_y)

#close window

window.close()
