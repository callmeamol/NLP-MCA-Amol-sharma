# TO FIND URL IN A SCENTENCE 
import re
sentence= "i love spending time on the website https://www.amol.com/" 
def find_url(text):
   return re.findall(r"https?://[^\s]+", text)
ab=find_url(sentence)
print(ab)
