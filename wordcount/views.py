
from django.http import HttpResponse
#this is to return an Http response like returning a string
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordcountdict= {}
    i=0
    #To filter out unneccessary commas etc
    for word in wordlist:
        if (ord(word[0])>65 and ord(word[0])<90) or (ord(word[0])>97 and ord(word[0])<122):
            i = i+1
        else:
            wordlist.pop(i)
            i = i+1
    for word in wordlist:
        if word in wordcountdict:
       #Increase
            wordcountdict[word] +=1
        else:
            #add to dictionary
            wordcountdict[word] = 1
    sortbykeydict = sorted(wordcountdict.items(), key = lambda t : t[1], reverse = True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'wordcountdict': sortbykeydict})
def aboutt(request):
    return render(request, 'about.html')

