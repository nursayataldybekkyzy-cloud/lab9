from django.shortcuts import render
from django.http import HttpResponse

# Басты бет
def index(request):
    return render(request, 'mainapp/index.html')

# Өзіңіз туралы бет
def about(request):
    return render(request, 'mainapp/about.html')

# Динамикалық жоба беті
def project_detail(request, project_id):
    return render(request, 'mainapp/project_detail.html', {'project_id': project_id})

# Техникалық бет (HttpResponse)
def info(request):
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    ip_address = request.META.get('REMOTE_ADDR', 'unknown')
    return HttpResponse(f"<h1>Пайдаланушы туралы ақпарат</h1><p>IP: {ip_address}, User-Agent: {user_agent}</p>")