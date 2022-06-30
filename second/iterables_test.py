def Sentence(sentence):
    count=0
    while count<len(sentence.split()):
         yield sentence.split()[count]
         count+=1

def sentence(sentence):
    for word in sentence.split():
        yield word
my_sentence=sentence('This is a test')
for word in my_sentence:    
    print(word)