from lxml import etree
from collections import Counter
import nltk

tree = etree.parse('news.xml')
root = tree.getroot()

for n in root[0]:
    print(f'{n[0].text}:')
    c = Counter(nltk.word_tokenize(n[1].text.lower()))
    print(*[i[1] for i in sorted([(i[1], i[0]) for i in c.most_common(7)], reverse=True)[:5]])

