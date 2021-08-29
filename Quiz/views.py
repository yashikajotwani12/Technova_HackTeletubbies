from django.shortcuts import render
from Quiz.models import Chapter

# Create your views here.
def crypto_chapters(request):
     chapters =   Chapter.objects.filter(category = "crypto")
     print(chapters)
     return render(request, 'chapters.html' , { 'chapter_list' : chapters, 'name': "Cryptocurrency Basics"} )

def earn_chapters(request):
     chapters= Chapter.objects.filter(category = "earn")
     print(chapters)
     return render(request, 'chapters.html' , { 'chapter_list' : chapters, 'name': "How to Earn Crypto ?"} )

def trade_chapters(request):
     chapters= Chapter.objects.filter(category = "trade")
     print(chapters)
     return render(request, 'chapters.html' , { 'chapter_list' : chapters, 'name': "How to Trade Crypto ?"} )

def chapterContent(request, id):
    chapter_content = Chapter.objects.get(pk = id)
    print (chapter_content)
    return render(request, 'chapter-content.html' ,{ 'chapter' : chapter_content} )