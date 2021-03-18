import pyperclip
clip_str = pyperclip.paste()
lines = clip_str.splitlines()
result_str = ""
for l in lines:    
    if l[-1] == ".":
        result_str += l
        result_str += "\r\n    "
    else:
        result_str += l        

pyperclip.copy(result_str)