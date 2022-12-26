import re
import pandas as pd

def lowercase(text):
    text_kecil = text.lower()
    return text_kecil

def remove_unnecessary_char(text):
    text = re.sub(r'\\n',' ', text) #remove every '\\n'
    text = re.sub('rt','', text) # remove every retweet symbol
    text = re.sub('user','', text) #remove every username
    text = re.sub('url','', text) #remove every url simbol
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))',' ',text) #remove url
    text = re.sub('  +',' ', text) #remove extra space
    text = re.sub(';','', text) #remove ;
    text = re.sub('\d+\.\s',' ', text)
    text = re.sub(r'x[a-z0-9][a-z0-9]', '', text)
    return text

def remove_nonaplhanumeric(text):
    text = re.sub(r'[^0-9a-zA-Z\?!,.]+',' ', text)
    text = re.sub('"', '', text)
    text = re.sub('\s\s+', ' ', text)
    text = re.sub('^\s', '', text)
    return text

def remove_duplicateexclamation(text):
    text = re.sub(r'[!]{2,}', '!', text)
    text = re.sub(r'[\?]{2,}', '?', text)
    text = re.sub(r'[! ]{2,}', '!', text)
    text = re.sub(r'[\? ]{2,}', '?', text)
    text = re.sub(r',{2,}', ',', text)
    text = re.sub(r'\.{2,}', '.', text)
    return text


def normalize_alay(text): 
    alay_dict = pd.read_csv('new_kamusalay.csv', encoding='latin-1', header=None)
    alay_dict = alay_dict.rename(columns={0: 'alay', 1: 'baku'})
    alay_dict_map = dict(zip(alay_dict['alay'], alay_dict['baku']))
    for word in alay_dict_map:
        normalize_baku = ' '.join([alay_dict_map[word] if word in alay_dict_map else word for word in text.split(' ')])
        return normalize_baku
    
    
def preprocess(text):
    text = lowercase(text)
    text = remove_unnecessary_char(text)
    text = remove_nonaplhanumeric(text)
    text = remove_duplicateexclamation(text)
    text = normalize_alay(text)
    text = lowercase(text)
    return text

list = ['a']