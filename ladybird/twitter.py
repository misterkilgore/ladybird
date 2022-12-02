import re

def clean_tweet(text):
    
    temp = text
    rp = False
    
    #Lowercase
    temp = temp.lower()
    
    # Remove @ refs
    temp = re.sub("@[A-Za-z0-9_]+","", temp)
    
    # Remove hashtags
    temp = re.sub("#[A-Za-z0-9_]+","", temp) 
    
    # Remove links
    temp = re.sub(r"http\S+", "", temp)
    temp = re.sub(r"www.\S+", "", temp)
    
    # Remove punctations
    
    if rp is True:
        temp = re.sub('[()!?]', ' ', temp)
        temp = re.sub('\[.*?\]',' ', temp)
    
    # Remove non-alphanumeric characters
    temp = re.sub("[^A-Za-z0-9]"," ", temp)
    
    return(temp)