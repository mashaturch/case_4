"""Case-study #3 Анализ текста
Разработчики:
Турчинович М. (40%), Зубарева Т. (40%), Костылев М. (35%);

"""

from textblob import TextBlob

#text input
text = input("Введите текст:")

count_sentens = text.count('.') + text.count('!') + text.count('?')  #number of proposals
count_words = text.count(" ") + 1  #word count
ASL = float(count_words/count_sentens)
count_syllables = 0
k = 0

#number of syllables
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

#output of results
print ('Предложений:', count_sentens)
print ('Слов:', count_words)
print ('Слогов:', count_syllables)
print ('Средняя длина предложения в словах:', ASL)
print ('Средняя длина слова в слогах:', ASW)
print ('Индекс удобочитаемости Флеша:', FRE)

if (text[0] in 'ЙЦУКЕЁНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'): #reading for Russian text
    if FRE > 80:
        print ('Текст очень легко читается (для младших школьников).')
    elif FRE > 50:
        print ('Простой текст (для школьников).')
    elif FRE > 25:
        print ('Текст немного трудно читать (для студентов).')
    else:
        print ('Текст трудно читается (для выпускников ВУЗов).')
else:   #reading for English text
    if FRE > 90:
        print ('Очень легко читать. Легко понимает средний 11-летний ученик.')
    elif FRE > 80:
        print ('Легко читать. Разговорный английский для потребителей..')
    elif FRE > 70:
        print ('Довольно легко читать.')
    elif FRE > 60:
        print('Обычный английский. Легко понимают учащиеся 13–15 лет..')
    elif FRE > 50:
        print('Довольно сложно читать.')
    elif FRE > 30:
        print ('Сложно читать.')
    elif FRE > 10:
        print ('Очень трудно читать. Лучше всего понимают выпускники университетов.')
    else:
        print ('Чрезвычайно трудно читать. Лучше всего понимают выпускники университетов.')

#finding the tonality of the text
if text_trans.polarity >= 0.3:
    tonality = 'положительная'
elif -0.3 <= text_trans.polarity <= 0.3:
    tonality = 'нейтральная'
else:
    tonality = 'негативная'

#output of results
print ('Тональность текста:', tonality)
print ('Объективность: {:.1f}%'.format ((1 - text_trans.subjectivity) * 100))
