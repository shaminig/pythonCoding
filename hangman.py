import random
list=['apple','mango','orange']
picked_word=random.choice(list)
print(picked_word)
print(len(picked_word))
word_bar=[]
for i in range(len(picked_word)):
    word_bar += '_'
print(word_bar)
# game_over=False
# while not game_over:
guessed_letter=input("guess a letter ")
for position in range(len(picked_word)):
    letter=picked_word[position]
    if(guessed_letter==letter):
         word_bar[position]=letter
         print(word_bar)
if guessed_letter not in picked_word:
    

