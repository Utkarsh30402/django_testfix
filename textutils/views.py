#I have created this file --dhruv

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

    
    #params = {'name':'dhruv','place':'mars'}
    #return render(request, 'test.html', params)
    

    #return HttpResponse('''<h1>Home</h1>''')

def analyze(request):

    #get text
    djtext = request.GET.get('text','default')

    #checkbox value
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    #print("removepunc is:",removepunc) #not needed
    #print(djtext)  #not needed


    #check which checkbox is on
    if removepunc =='on':

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char

        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed}

    #returning text
        return render(request,'analyze.html', params)
    
    #analyzing text
    elif fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {'purpose':'Changed to Uppercase', 'analyzed_text':analyzed}

    #returning text
        return render(request,'analyze.html', params)


    elif newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        
        params = {'purpose':'Newline Removed', 'analyzed_text':analyzed}

    #returning text
        return render(request,'analyze.html', params)



    else:
        return HttpResponse("Error")

# def capitalizefirst(request):
#     return HttpResponse('''Capitalizefirst''')

# def newlineremove(request):
#     return HttpResponse("Newline remove")

# def spaceremove(request):
#     return HttpResponse("Space remove <br> <a href='/'>back</a>")

# def charcount(request):
#     return HttpResponse("char count")


def about(request):
    return render(request, 'about.html')
    #return HttpResponse("about <br> <a href='/'>back</a>")
