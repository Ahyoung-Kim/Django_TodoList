from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
  form = TodoForm()
  todos = Todo.objects.filter().order_by('date')

  return render(request, 'index.html', {'todos': todos, 'form': form})


def todo_form(request):
  # POST 요청 -> 작성한 폼 가져와서 DB 에 저장하고 'home'으로 이동
  if request.method == 'POST' or request.method == 'FILES':
    form = TodoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')

  # GET 요청이면 home으로
  return redirect('home')

  # return render(request, 'todo_form.html', {'form': form})


def delete_todo(req, pk):
  todo = get_object_or_404(Todo, id=pk)
  todo.delete()
  return redirect('home')


def edit_todo(req, pk):
  todo = get_object_or_404(Todo, id=pk)

  if todo.edit == False:
    todo.edit = True
  else:
    todo.edit = False

  todo.save()
  return redirect('home')

def edit_post(req, pk):
  todo = get_object_or_404(Todo, id=pk)

  if req.method == 'POST':
    todo.contents = req.POST['edit_contents']
    todo.edit = False
    todo.save()

  return redirect('home')


def complete_todo(req, pk):
  todo = get_object_or_404(Todo, id=pk)

  if todo.complete == False:
    todo.complete = True
  else:
    todo.complete = False

  todo.save()
  
  return redirect('home')