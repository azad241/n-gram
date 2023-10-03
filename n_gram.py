import collections
import nltk
import pandas as pd

df = pd.read_csv('apn fa ski.csv')
list_of_keywords = df['query'].tolist()
list_of_words_in_keywords = [x.split(" ") for x in list_of_keywords]
counts = collections.Counter()
for phrase in list_of_words_in_keywords:
  #counts.update(nltk.ngrams(phrase, 1))
  counts.update(nltk.ngrams(phrase, 2))
  #counts.update(nltk.ngrams(phrase, 3))


top =counts.most_common(50)
x = pd.DataFrame(top, columns=['query','count'])

#Retrieve volume for each n-grams
def GetVolume(query):
  x = df[df['query'].str.contains(query)]
  return x['impressions'].sum()

#Remove useless characters
def RemoveUselessChar(x):
  output=''
  for element in x:
    if "'" == element:
      continue
    elif '('==element:
      continue
    elif ')' == element:
      continue
    else:
      output+= ' ' +element
  output = output.strip()
  return output

x['query'] = x['query'].apply(RemoveUselessChar)
x['query'] = x['query'].str.replace(',',' ')
x['Volume'] = x['query'].apply(GetVolume)

print(x)
