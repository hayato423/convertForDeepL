import pyperclip
clip_str = pyperclip.paste()
strings = clip_str.split(".")
strings.pop(len(strings)-1)
result_str = ""
for s in strings:
    s = s.replace("\r\n","")
    s = s + ".\r\n"
    result_str += s
    print(s,end="")
pyperclip.copy(result_str)
