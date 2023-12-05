import pyautogui
import pyperclip
import time

class WebbasedChatGPTControl():

    """
    Controls a web-based ChatGPT interface using PyAutoGUI.

    Parameters:
        messagebox_x (int): X-coordinate of the messagebox in ChatGPT.
        messagebox_y (int): Y-coordinate of the messagebox in ChatGPT.
        startdrag_x (int): X-coordinate to start dragging the mouse.
        startdrag_y (int): Y-coordinate to start dragging the mouse.
        enddrag_x (int): X-coordinate to end dragging the mouse.
        enddrag_y (int): Y-coordinate to end dragging the mouse.
        answer_waittime (float): Number of seconds to wait for ChatGPT to answer.

    Methods:
        ask_question(question):
            Asks a question to ChatGPT and retrieves its answer.

    Example Usage:
        chat_control = WebbasedChatGPTControl(740, 975, 1500, 930, 1500, 150, 10)
        answer = chat_control.ask_question("What is the meaning of life?")
        print(answer)
    """

    def __init__(self, messagebox_x, messagebox_y, startdrag_x, startdrag_y, enddrag_x, enddrag_y, answer_waittime):
        """
        Initialize the WebbasedChatGPTControl instance.

        Parameters:
            messagebox_x (int): X-coordinate of the messagebox in ChatGPT.
            messagebox_y (int): Y-coordinate of the messagebox in ChatGPT.
            startdrag_x (int): X-coordinate to start dragging the mouse.
            startdrag_y (int): Y-coordinate to start dragging the mouse.
            enddrag_x (int): X-coordinate to end dragging the mouse.
            enddrag_y (int): Y-coordinate to end dragging the mouse.
            answer_waittime (int): Number of seconds to wait for ChatGPT to answer.
        """
        # Initialize instance variables
        self.MESSAGEBOX_POS 	= {'x': messagebox_x, 'y': messagebox_y}	
        self.STARTDRAG_POS 	    = {'x': startdrag_x, 'y': startdrag_y}		
        self.ENDDRAG_POS 	    = {'x': enddrag_x, 'y': enddrag_y}		    
        self.ANSWER_WAITTIME    = answer_waittime	                        
    
    def ask_question(self, question):
        """
        Ask a question to ChatGPT and retrieve its answer.

        Parameters:
            question (str): The question to ask.

        Returns:
            str: The answer provided by ChatGPT.
        """

        SCROLLDOWN_PIXELS = 10000                                           # Number of pixels to scroll down before dragging.
        
        pyautogui.click(self.MESSAGEBOX_POS['x'], self.MESSAGEBOX_POS['y'])	# Click inside the messagebox of ChatGPT
        pyautogui.typewrite(question)								        # Paste the question
        pyautogui.press('enter')									        # Press <enter>

        time.sleep(self.ANSWER_WAITTIME)                                    # Wait some time for ChatGPT to display its answer

        # Select and copy the answer and all text above
        pyperclip.copy("") 											        # Empty the clipboard
        pyautogui.moveTo(self.STARTDRAG_POS['x'], self.STARTDRAG_POS['y'])	# Move to the place to start dragging
        pyautogui.scroll(-1*SCROLLDOWN_PIXELS)										        # Scroll text down to make sure the answer is shown
        pyautogui.mouseDown(button='left')							        # Mouse down
        pyautogui.moveTo(self.ENDDRAG_POS['x'], self.ENDDRAG_POS['y'], 1)	# Drag over the text in 1 second
        pyautogui.mouseUp()											        # Mouse up
        pyautogui.hotkey('ctrl', 'c')								        # Copy the selected text
        pyautogui.click(self.STARTDRAG_POS['x'], self.STARTDRAG_POS['y'])	# Click at the starting point of the dragging to deselect the text


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

        return answertext # The extracted answer
        