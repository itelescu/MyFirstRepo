from urllib.request import urlopen 

def feach_words():

    story= urlopen('http://sixty-north.com/c/t.txt')
    story_words=[]
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()

# print (story_words)

    for word in story_words:
        print (word)


if __name__== '__main__':
    feach_words()

