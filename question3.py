# to find hashtags in a scentence 
import re
scentence="hi this is me #AMOL"
def find_hashtags(texts):
    return re.findall(r'#\w+',texts)
ab= find_hashtags(scentence)
print(ab)
