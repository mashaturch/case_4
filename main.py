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
    if (text[k] in 'aeiouAEIOUауоиэыяюеёАУОИЭЫЯЮЕЁ'):
        count_syllables += 1
    k = k+1
ASW = float(count_syllables/count_words)
if (text[0] in 'ЙЦУКЕЁНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'):
    FRE = 206.835-(1.3*ASL)-(60.1*ASW)
else:
    FRE = 206.835-(1.015*ASL)-(84.6*ASW)


print ('Предложений:', count_sentens)
print ('Слов:', count_words)
print ('Слогов:', count_syllables)
print ('Средняя длина предложения в словах:', ASL)
print ('Средняя длина слова в слогах:', ASW)
print ('Индекс удобочитаемости Флеша:', FRE)
blob = TextBlob(text)
trans = text
print (trans)
print ('Тональность текста: ')
if (blob.detect_language() != 'en'):
    trans = blob.translate(to = 'en')
    print ('Объективность:', (1 - trans.subjectivity))
else:
    print ('Объективность:', (1 - TextBlob(text).subjectivity))
