from lxml import etree
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string

tree = etree.parse('news.xml')
root = tree.getroot()
lemmatizer = nltk.WordNetLemmatizer()

for n in root[0]:
    print(f'{n[0].text}:')
    lemmas = []
    tokenized = nltk.word_tokenize(n[1].text.lower())
    lemmatized = [lemmatizer.lemmatize(i) for i in tokenized]
    for l in lemmatized:
        if l in string.punctuation or l in stopwords.words('english'):
            continue
        lemmas.append(lemmatizer.lemmatize(l))

    c = Counter(lemmas)
    print(*[i[1] for i in sorted([(i[1], i[0]) for i in c.most_common(50)], reverse=True)[:5]])

