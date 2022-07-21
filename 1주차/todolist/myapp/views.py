from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
  todos = Todo.objects.filter().order_by('date')
  return render(request, 'index.html', {'todos': todos})

def todo_form(request):
  # POST 요청 -> 작성한 폼 가져와서 DB 에 저장하고 'home'으로 이동
  if request.method == 'POST' or request.method == 'FILES':
    form = TodoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')

  # GET 요청이면 폼 보여주기
  else:
    form = TodoForm()

  return render(request, 'todo_form.html', {'form': form})


def delete_todo(req, pk):
  todo = get_object_or_404(Todo, id=pk)
  todo.delete()
  return redirect('home')


def edit_todo(req, pk):
  todo = get_object_or_404(Todo, id=pk)

  if req.method == 'POST':
    todo.contents = req.POST['contents']
    todo.save()
    return redirect('home')

  else:
    form = TodoForm()
    return render(req, 'update.html', {'form': form})