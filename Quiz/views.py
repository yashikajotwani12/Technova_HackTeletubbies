from django.shortcuts import render
from Quiz.models import Chapter

# Create your views here.
def chapters(request):
     chapters= Chapter.objects.all()
     print(chapters)
     return render(request, 'chapters.html' , { 'chapter_list' : chapters} )

def chapterContent(request, id):
    chapter_content = Chapter.objects.get(pk = id)
    print (chapter_content)
    return render(request, 'chapter-content.html' ,{ 'chapter' : chapter_content} )