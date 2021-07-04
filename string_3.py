# Даний текст. Здійснити в цьому тексті пошук і заміну заданої фрази.

text = 'Даний текст. Здійснити в цьому тексті пошук і заміну заданої фрази.'
print(text)

phrase = input('Which phrase in the text do you want to change?: ')
changing = input('Print new phrase, please: ')

updated_text = text.replace(phrase, changing)

print(updated_text)