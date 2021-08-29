from django.shortcuts import render

# Create your views here.
def chapters(request):
    return render(request, 'chapters.html' )

def chapterContent(request):
    return render(request, 'chapter-content.html' )