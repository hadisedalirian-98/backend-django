from django.shortcuts import render

# Create your views here.
# views.py در myapp  
from django.shortcuts import render  

def home(request):  
    return render(request, 'index.html')  # فرض بر این است که شما یک فایل قالب به نام index.html دارید