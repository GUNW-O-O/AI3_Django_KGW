from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

from .forms import TodoForm


from .models import * # models 의 모든 모델 import

# Create your views here.
def index(request):
    print('메인 화면...')
    return render(request, 'todo/index.html', {})

def todo(request):
    wait_list = Todo.objects.filter(status='WAIT')
    ing_list = Todo.objects.filter(Q(status='ING') | Q(status='DONE')).order_by('-status')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:todo')  # 등록 성공하면 메인 페이지로 리다이렉트
    else:
        form = TodoForm()

    context = {
        'wait_list': wait_list,
        'ing_list': ing_list,
        'form': form,
    }
    return render(request, 'todo/todo.html', context)

# def create(request):
#     print('할 일 등록...')
#     todos = Todo.objects.all().order_by('-status')
#     # POST 방식의 파라미터
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('todo:todo')
#         else:
#             # 유효성 실패 시 폼과 리스트를 함께 렌더링
#             return render(request, 'todo/todo.html', {'form': form, 'todos': todos})
#     else:
#         form = TodoForm()
#     # 할 일 목록으로 리다이렉트
#     return render(request, 'todo/todo.html', {'form': form})

def delete(request, todo_no):
    print('삭제 요청...')
    # 파라미터
    todo_no = request.POST['todo_no']
    print('no : {}'.format(todo_no))
    try:
        todo = Todo.objects.get(no=todo_no)
        todo.delete()   # 할 일 삭제 요청
    except Todo.DoesNotExist:
        print('삭제할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo:todo'))

def ing(request):
    print('진행 상태로 변경...')
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        # 할 일 상태 수정
        todo.status = 'ING'
        todo.is_completed = False
        todo.save()
    except Todo.DoesNotExist:
        print('수정할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo:todo'))

def done(request):
    print('완료 상태로 변경...')
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        # 할 일 상태 수정
        if todo.status == 'DONE':
            todo.status = 'ING'
        else:
            todo.status = 'DONE'
            todo.is_completed = True
        todo.save()
    except Todo.DoesNotExist:
        print('수정할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo:todo'))

def wait(request):
    print('대기 상태로 변경...')
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        # 할 일 상태 수정
        todo.status = 'WAIT'
        todo.is_completed = False
        todo.save()
    except Todo.DoesNotExist:
        print('수정할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo:todo'))

def read(request, todo_no):
    todo = Todo.objects.get(no=todo_no)
    
    return render(request, 'todo/read.html', {'todo' : todo})

def update(request, todo_no):
    todo = get_object_or_404(Todo, no=todo_no)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:read', todo_no=todo.no)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/update.html', {'form': form, 'todo':todo})