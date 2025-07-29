# TO FIND EMAIL IN A SCENTENCE 
import re
sentence= "this is my mail id callmeamol@gmail.com"
def find_emails(text):
  return re.findall(r'[\w.-]+@[\w.-]+', text)
ab=find_emails(sentence)
print(ab)

