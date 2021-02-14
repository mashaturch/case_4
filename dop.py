from main import text
count_sentens = text.count('.') + text.count('!') + text.count('?')
ASL = count_words/count_sentens
count_words = text.count(" ") + 1
ASW = count_syllables/count_words
