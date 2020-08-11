from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt     #it is do display out wordcloud

from PIL import Image       #it is to load the image
import numpy as np          #it is to get the color of the image

text = open('common.txt', 'r').read()
stopwords = set(STOPWORDS)

#Appearance
custom_mask = np.array(Image.open(path.join(d, 'skull.png')))
wc = WordCloud(background_color = 'white',
        stopwords = stopwords,
        mask = custom_mask,
        contour_width = 3,
        contour_color = 'black')

wc.generate(text)
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)

#plotting image
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()


wc.to_file('skull_wordcloud.png')
