'''
Webbased ChatGPT control

This programs controls the webbased version of ChatGPT with the help of pyautogui and pyperclip.
It pastes a question in ChatGPT and then copies the answer from the webpage, like a human would do.

'''

import pyautogui
import pyperclip
import time

MESSAGEBOX_POS 	= {'x': 740, 'y': 975}		# Coördinates to click inside the messagebox of ChatGPT
STARTDRAG_POS 	= {'x': 1500, 'y': 930}		# Coördinates of the postion to start dragging the mouse
ENDDRAG_POS 	= {'x': 1500, 'y': 150}		# Coördinates of the postion to start dragging the mouse
ANSWER_WAITTIME = 10						# Number of seconds to wait so that ChatGPT can answer


question = 'Wat is de wortel van 39 (ongeveer)?'


# Ask ChatGPT a question
pyautogui.click(MESSAGEBOX_POS['x'], MESSAGEBOX_POS['y'])	# Click inside the messagebox of ChatGPT
pyautogui.typewrite(question)								# Paste the question
pyautogui.press('enter')									# Press <enter>

# Wait some time for ChatGPT to display its answer
time.sleep(ANSWER_WAITTIME)

# Select and copy the answer and all text above
pyperclip.copy("") 											# Empty the clipboard
pyautogui.moveTo(STARTDRAG_POS['x'], STARTDRAG_POS['y'])	# Move to the place to start dragging
pyautogui.scroll(-1500)										# Scroll text down to make sure the answer is shown
pyautogui.mouseDown(button='left')							# Mouse down
pyautogui.moveTo(ENDDRAG_POS['x'], ENDDRAG_POS['y'], 1)		# Drag over the text in 1 second
pyautogui.mouseUp()											# Mouse up
pyautogui.hotkey('ctrl', 'c')								# Copy the selected text
pyautogui.click(STARTDRAG_POS['x'], STARTDRAG_POS['y'])								# Click at the starting point of the dragging to deselect the text


# Extract the answer from the selected text
pasted_text = pyperclip.paste()		# Paste text from clipboard
lines = pasted_text.splitlines()	# Split it into lines.
answer=[] 							# Array of lines to store the answer
startadding_lines = False					# Becomes True if a line contains 'ChatGPT' and becomes False if a line contains 'User'

for l in lines:	
	if len(l) > 0:					# Skip empty lines
		if startadding_lines:		# Add lines if toggle is True
			answer.append(l)
		if 	'ChatGPT' in l:			# Set toggle to True if a line contains 'ChatGPT'; lines following this line will be added.
			startadding_lines=True
		if "User" in l:				# Set toggle to False if a line contains 'User'
			startadding_lines=False	
			answer=[]				# Also empty the array with lines as they are not part of the answer.


answertext = '\n'.join(answer)		# Combine answerlines into a string

print(answertext)