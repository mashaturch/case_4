from main import text
count_sentens = text.count('.') + text.count('!') + text.count('?')
ASL = count_words/count_sentens
count_words = text.count(" ") + 1
ASW = count_syllables/count_words
text = input()
count_syllables = 0
k = 0
while k < len(text):
    if text[k] in 'aeiouAEIOUауоиэыяюеёАУОИЭЫЯЮЕЁ':
        count_syllables += 1
    k = k+1
FRE = 206.835-(1.3*ASL)-(60.1*ASW)
Print ()
print ()