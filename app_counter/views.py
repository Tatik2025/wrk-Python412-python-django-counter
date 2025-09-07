from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from app_counter.models import Counter


def index(request):

    counters = Counter.objects.filter(is_favorite=True)

    return render(
        request=request,
        template_name="app_counter/index.html",
        context={
            "counters": counters
        }
    )


@login_required
def counter(request):

    try:
        counters = Counter.objects.filter(user=request.user)
    except Counter.DoesNotExist:
        counters = None

    return render(
        request=request,
        template_name="app_counter/counter.html",
        context={
            "counters": counters
        }
    )


@login_required
def create_counter(request):
    counter = Counter.objects.create(user=request.user)
    counter.save()

    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))


@login_required
def increase_counter(request, counter_id):

    Counter.objects.filter(pk=counter_id).update(value=F('value') + 1)

    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))


@login_required
def decrease_counter(request, counter_id):
    Counter.objects.filter(pk=counter_id).update(value=F('value') - 1)

    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))

@login_required
def delete_counter(request, counter_id):

    try:
        counter = Counter.objects.get(pk=counter_id)
        counter.delete()
    except Counter.DoesNotExist:
        pass

    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))

@login_required
def is_favorite_counter(request, counter_id):
    if Counter.objects.get(pk=counter_id).is_favorite:
        count = Counter.objects.get(pk=counter_id)
        count.is_favorite = False
        count.save()
    else:
        Counter.objects.filter(user=request.user).update(is_favorite=False)
        Counter.objects.filter(pk=counter_id).update(is_favorite=True)


    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))