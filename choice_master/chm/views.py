"""
Views for app chm
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from chm.models import Question
from chm.forms import QuizForm
from chm.forms import Quiz


@login_required
def index(request):
    """ If the user is authenticated redirect to login,
    otherwise display index page.
    """
    context = {}
    if request.user.is_staff:
        nfq = Question.objects.filter(flags__isnull=False).count()
        context['n_flagged_questions'] = nfq
    return render(request, 'index.html', context)


@login_required
def new_quiz(request):
    """ User wants to start an exam."""

    if request.method == 'POST':
        form = QuizForm(request.POST, user=request.user)
        if form.is_valid():
            quiz = form.make_quiz()
            return render(request, 'quiz.html', {'quiz': quiz.to_json()})
    else:
        form = QuizForm()

    return render(request, 'new_quiz.html', {'form': form})


def timer(request):
    seconds = request.GET.get('seconds', 10)
    return render(request, 'timer.html', {'seconds': seconds})


def quiz_results(request):
    return render(request, 'quiz_results.html', {'quiz': Quiz.objects.all()[0]})


def flag_question(request, id):
    # TODO: continue here
    seconds = request.GET.get('seconds', 10)
    return render(request, 'timer.html', {'seconds': seconds})
