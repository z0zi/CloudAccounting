from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Questions,Choices
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
# def index(request):
#     lastest_question_list=Questions.objects.order_by('pub_date')[0:5]
#     content={
#         'lastest_question_list':lastest_question_list
#     }
#     return render(request,'polls/index.html',content)
#     # return HttpResponse("Hello, world. You're at the polls index.")
#
# def detail(request,question_id):
#     question=get_object_or_404(Questions,id=question_id)
#     context={'question':question}
#     return render(request,'polls/detail.html',context)
#
# def results(request,question_id):
#     question = get_object_or_404(Questions, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
# def vote(request, question_id):
#     question=get_object_or_404(Questions,id=question_id)
#
#     try:lastest_question_list
#         selected_choice = question.choices_set.get(pk=request.POST['choice'])
#     except (KeyError,Choices.DoesNotExist):
#         return render(request,'polls/detail.html',{'question':question,
#                                                    'error_message': "You didn't select a choice.",})
#     else:
#         selected_choice.votes+=1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[0:5]


class DetailView(generic.DetailView):
    model = Questions
    template_name = 'polls/detail.html'
    queryset = Questions.objects.filter(pub_date__lte=timezone.now())



class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'

def vote(request, question_id):
    question=get_object_or_404(Questions,id=question_id)

    try:
        selected_choice = question.choices_set.get(pk=request.POST['choice'])
    except (KeyError,Choices.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,
                                                   'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
