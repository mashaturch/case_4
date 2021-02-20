"""Case-study #3 Анализ текста
Разработчики:
Турчинович М., Зубарева Т., Костылев М.;

"""

from textblob import TextBlob
text = input("Введите текст:")

count_sentens = text.count('.') + text.count('!') + text.count('?')
count_words = text.count(" ") + 1
ASL = float(count_words/count_sentens)
count_syllables = 0
k = 0
while k < len(text):
    if (text[k] in 'aeiouyAEIOUYауоиэыяюеёАУОИЭЫЯЮЕЁ'):
        count_syllables += 1
    k = k+1
ASW = float(count_syllables/count_words)
if (text[0] in 'ЙЦУКЕЁНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'):  #russian text
    FRE = 206.835-(1.3*ASL)-(60.1*ASW)
    text_trans = TextBlob(text)
    text_trans = text_trans.translate()
else:
    FRE = 206.835-(1.015*ASL)-(84.6*ASW)  #english text
    text_trans = TextBlob(text)


print ('Предложений:', count_sentens)
print ('Слов:', count_words)
print ('Слогов:', count_syllables)
print ('Средняя длина предложения в словах:', ASL)
print ('Средняя длина слова в слогах:', ASW)
print ('Индекс удобочитаемости Флеша:', FRE)

print (text_trans)
if text_trans.polarity >= 0.3:
    tonality = 'положительная'
elif -0.3 <= text_trans.polarity <= 0.3:
    tonality = 'нейтральная'
else:
    tonality = 'негативная'
print ('Тональность текста: ', tonality)
print ('Объективность: {:.1f}%'.format ((1 - text_trans.subjectivity) * 100))
