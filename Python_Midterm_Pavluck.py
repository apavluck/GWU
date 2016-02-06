#############################################
# Will count the number of lines in a file
#############################################
def CountLines(f):
    line_num = 0

    # Open file, read-only
    txtfile = open(f, 'r')

    for w in txtfile:
        line_num += 1

    return line_num

#############################################
# Will count the number of words in a file
#############################################
def CountWords(f):
    words = []
    word_num = 0

    txtfile = open(f, 'r')

    # Loop through the file
    for w in txtfile:
        word = w.split()
        words += word

    # Loop through all words in list
    for word in words:
        word_num += 1

    return word_num

#############################################
# Will count the number of characters in a file
#############################################
def CountCharacters(f):
    char_num=0
    words = []

    # Open file, read-only
    txtfile = open(f, 'r')

    # Loop through the file
    for w in txtfile:
        word = w.split()
        words += word

    for word in words:
        for char in word:
            char_num += 1
    return char_num

#############################################
# Will count the number of occurrences in a file
#############################################
def CountOccurrences(f, whatword):
    # Open file, read-only
    txtfile = open(f, 'r')

    words = []
    word_num = 0

    txtfile = open(f, 'r')

    # Loop through the file
    for w in txtfile:
        word = w.split()
        words += word

    return words.count(whatword)





word = "Lorem"
f = "Spring2016_2.txt"

print "\nThere are", CountLines(f), "lines in this file."
print "\nThere are", CountWords(f), "words in this file."
print "\nThere are", CountCharacters(f), "characters in this file."
print "\nThe word,", word,"is in this file", CountOccurrences(f, word), "times."