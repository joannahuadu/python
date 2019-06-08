from wordcloud import WordCloud, STOPWORDS
import jieba
from matplotlib import pyplot as plt
fig,ax=plt.subplots()

with open('freqword_n.txt','rb') as f:
    text=f.read()

wsplit=jieba.cut(text)
words="".join(wsplit)

mycloudword=WordCloud(font_path='simhei.ttf',
                      width=800, 
                      height=600, 
                      scale=1, 
                      margin=2,
                      background_color='white',
                      max_words=200, 
                      min_font_size=40, 
                      max_font_size=140,
                      stopwords=STOPWORDS, 
                      random_state=50).generate(words)

ax.imshow(mycloudword)
ax.axis("off")
plt.show()

mycloudword.to_file("freqword.png")
