with open("ywmapnpcdialog.txt", "r", encoding="utf8") as f:
  YWtext = f.read()
# could use regex, but lazyness says no.
while YWtext.find("<") != -1:
  YWtext = YWtext[:YWtext.find("<")] + YWtext[YWtext.find(">")+1:] 
while YWtext.find("[") != -1:
  YWtext = \
    YWtext[:YWtext.find("[")] + \
    YWtext[YWtext.find("[")+1:YWtext.find("]")-1].split("/")[0] + \
    YWtext[YWtext.find("]")+1:] 
while YWtext.find("\\n") != -1:
  YWtext = \
    YWtext[:YWtext.find("\\n")] + \
    YWtext[YWtext.find("\\n")+2:] 

with open("ywmapnpcdialogAUTOMATED.txt", "w", encoding="utf8") as f:
  f.write(YWtext)