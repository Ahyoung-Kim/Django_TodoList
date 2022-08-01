from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm
from .models import CurrDate

# Create your views here.
def home(request):
  form = TodoForm()
  todos = Todo.objects.filter().order_by('date')
  dates = CurrDate.objects.all()

  return render(request, 'index.html', 
    {'todos': todos, 'form': form, 'dates': dates})


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
  print('current path: ',req.path)
  todo = get_object_or_404(Todo, id=pk)
  y = todo.day.year
  m = todo.day.month
  d = todo.day.date
  print(y, m, d)

  if todo.complete == False:
    todo.complete = True
  else:
    todo.complete = False

  todo.save()
  
  form = TodoForm()
  
  # return redirect('home')
  return redirect('calender')



def calendar(req):
  form = TodoForm()

  return render(req, 'calendar.html')
  
def getDate(req):
  year = req.GET.get('year', None)
  month = req.GET.get('month', None)
  date = req.GET.get('date', None)

  return year, month, date

def calendar_get(req):
  form = TodoForm()

  # year = req.GET.get('year', None)
  # month = req.GET.get('month', None)
  # date = req.GET.get('date', None)

  year, month, date = getDate(req)
  print('test getDate: ', year, month, date)
  flag = True

  try:
      currDate = CurrDate.objects.get(year=year, month=month, date=date)
  except CurrDate.DoesNotExist: # if not, send DoesNotExist
      # raise Http404("Question does not exist") #what specific message to show
      print("404 error")
      flag = False
      currDate = CurrDate()
      currDate.year = year
      currDate.month = month
      currDate.date = date
      currDate.save()

  print('currDate: ', currDate)

  if req.method == 'POST' or req.method == 'FILES':
    print(year, month, date)
    filled = TodoForm(req.POST, req.FILES)
    if filled.is_valid():
      unfinished = filled.save(commit=False)
      unfinished.day = currDate
      unfinished.save()
      currDate.cnt = currDate.cnt + 1
      currDate.save()
  
  return render(req, 'calendar.html', {
    'year': year, 'month': month, 'date': date,
    'flag': flag, 'form': form, 'currDate': currDate
  })


def calendar_delete(req, pk):

  year, month, date = getDate(req)

  todo = get_object_or_404(Todo, id=pk)
  currDate = todo.day
  todo.delete()

  form = TodoForm()
  currDate.cnt = currDate.cnt - 1
  currDate.save()

  return render(req, 'calendar.html', {
    'year': year, 'month': month, 'date': date,
    'form': form, 'currDate': currDate
  })


def calendar_complete(req, pk):
  year, month, date = getDate(req)

  todo = get_object_or_404(Todo, id=pk)
  currDate = todo.day

  if todo.complete == False:
    todo.complete = True
  else:
    todo.complete = False

  todo.save()
  
  form = TodoForm()
  
  return render(req, 'calendar.html', {
    'year': year, 'month': month, 'date': date,
    'form': form, 'currDate': currDate
  })

def calendar_edit(req, pk):
  year, month, date = getDate(req)
  todo = get_object_or_404(Todo, id=pk)
  currDate = todo.day
  form = TodoForm()

  if todo.edit == False:
    todo.edit = True
  else:
    todo.edit = False

  todo.save()
  return render(req, 'calendar.html', {
    'year': year, 'month': month, 'date': date,
    'form': form, 'currDate': currDate
  })


def calendar_edit_post(req, pk):
  year, month, date = getDate(req)
  todo = get_object_or_404(Todo, id=pk)
  currDate = todo.day
  form = TodoForm()

  if req.method == 'POST':
    todo.contents = req.POST['edit_contents']
    todo.edit = False
    todo.save()

  return render(req, 'calendar.html', {
    'year': year, 'month': month, 'date': date,
    'form': form, 'currDate': currDate
  })