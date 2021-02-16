from main import text

count_sentens = text.count('.') + text.count('!') + text.count('?')
count_words = text.count(" ") + 1
ASL = count_words/count_sentens
ASW = count_syllables/count_words
count_syllables = 0
k = 0
while k < len(text):
    if (text[k] in 'aeiouAEIOUауоиэыяюеёАУОИЭЫЯЮЕЁ'):
        count_syllables += 1
    k = k+1
if (text[0] in 'ЙЦУКЕЁНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'):
    FRE = 206.835-(1.3*ASL)-(60.1*ASW)
else:
    FRE = 206.835-1.015(count_words/count_sentens)-84.6(count_syllables/count_words)