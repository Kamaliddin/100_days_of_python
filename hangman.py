from random import *

random_words = ['banana', 'stoicism', 'notebook', 'computer', 'terraformation', 'mars']
word = choice(random_words)
blanks = ['_' for i in range(len(word))]
print(f'Psst, the hint: {word}')
print(''.join(blanks))
stages = ['''
    +----+
    |    |
    x    |
   /|\   |
   / \   |
         |
 ==========
    ''', ''' 
    +----+
    |    |
    0    |
   /|\   |
   / \   |
         |
 ==========
''', ''' 
    +----+
    |    |
    0    |
   /|\   |
         |
         |
 ==========
''', ''' 
    +----+
    |    |
    0    |
         |
         |
         |
 ==========
''', ''' 
    +----+
    |    |
         |
         |
         |
         |
 ==========
''']
lives = 4
i = 0

while '_' in blanks:
    guess = input('Guess the letter: ')
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            blanks[position] = letter
    if guess not in word:
        if lives != 0:
            lives -= 1
            print(stages[lives])
        else:
            break
        

    print(''.join(blanks))
    
if '_' not in blanks:
    print('You won!')
elif lives == 0:
    print('You lost!')