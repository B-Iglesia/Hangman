import random

words = open('popular.txt','r')
word_list = []
for i in words.readlines():
    i = i[0:len(i)-1]
    word_list.append(i)
def main():
    print("Let's play HangMan!")
    guessed = []
    indx = random.randint(1,len(word_list))
    word = word_list[indx]
    view = ['_'] * len(word)
    while len(guessed) != 26:
        print()
        print("Guessed Letters")
        print(guessed)
        
        print("The word")
        print(' '.join(view))
        a = str(input('Guess a letter! '))
        if a in word:
            for i in range(0,len(word)):
                if word[i] == a:
                    view[i] = a
        if a not in word:
            guessed.append(a)
        if a in guessed:
            print("You already tried that!")
        if ''.join(view) == word:
            break
        
    if len(guessed) == 26:
        print("Sorry! The word was, " , word)
    else:
        print("Congratulations! The word was ", word,'!')
        
if __name__ == "__main__":
    main()
    