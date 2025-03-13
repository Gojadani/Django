from django.shortcuts import render
tasks = ["limpiar el banio", "sacar la basura", "barrer la casa"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks" : tasks
    })