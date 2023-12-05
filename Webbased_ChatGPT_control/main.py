from WebbasedChatGPTControl import WebbasedChatGPTControl as wcc


chat = wcc(messagebox_x = 740, 
           messagebox_y = 975,
           startdrag_x  = 1500,
           startdrag_y  = 930,
           enddrag_x    = 1500,
           enddrag_y    = 135,
           answer_waittime = 10)

print(chat.ask_question("Wanneer valt moederdag op 12 mei in Nederland?"))