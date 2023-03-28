def clean_word(word):
     return list(filter(lambda x:x.isalpha(),word))

def  count_words(text):
     
    return {i:len(clean_word(i)) for i in text.split()}
     
    
print(count_words("gh hggyg"))