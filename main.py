"""Case-study #3 Анализ текста
Разработчики:
Турчинович М., Зубарева Т., Костылев М.;

"""


import dop as d
text = input("Введите текст:")


print ('Предложений:', d.count_sentens)
print ('Слов:', d.count_words)
print ('Слогов:', d.count_syllables)
print ('Средняя длина предложения в словах:', d.ASL)
print ('Средняя длина слова в слогах:', d.ASW)
print ('Индекс удобочитаемости Флеша:', d.FRE)

