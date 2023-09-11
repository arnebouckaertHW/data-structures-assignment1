# Vocabulary of translator
english_vocabulary = ["hello", "yes", "no", "yellow", "dog", "table", "book"]
french_vocabulary = ["bonjour", "oui", "non", "jaune", "chien", "table", "livre"]
german_vocabulary = ["hallo", "jawohl", "nein", "gelb", "hund", "tisch", "buchen"]

# Ask for word
word = input("Please enter an English word. \nI will give you the French and German translation: ")

# Check if word is in vocabulary and translate
word_found = False
i = 0
while (i < len(english_vocabulary)):
    if english_vocabulary[i] == word:
        print("The French translation is %s. \nThe German translation is %s" % (french_vocabulary[i], german_vocabulary[i]))
        word_found = True
        break
    i += 1

if word_found == False:
    print("The English word %s is not in my vocabulary." % word)