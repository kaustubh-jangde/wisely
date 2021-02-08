from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
import datetime
from . models import morning_entry, evening_entry, anchor
import json
import cryptocode

# Create your views here.


def index_view(request):
    return render(request, 'wisely/index.html', context={})


@login_required(login_url='/register/login/')
def morning_view(request):
    max_date = datetime.date.today()
    max_date = max_date.strftime("%Y-%m-%d")

    val_dict = {
        'thoughts': '',
        'iut1': '',
        'iut2': '',
        'iut3': '',
        'iut4': '',
        'todo': '',
        'not_to_do': ''
    }

    if request.method == 'POST':
        thoughts = request.POST["thoughts"]
        iut1 = request.POST["iut1"]
        iut2 = request.POST["iut2"]
        iut3 = request.POST["iut3"]
        iut4 = request.POST["iut4"]
        todo = request.POST["todo"]
        not_to_do = request.POST["not_to_do"]
        date = request.POST["date"]

        val_dict['thoughts'] = thoughts
        val_dict['iut1'] = iut1
        val_dict['iut2'] = iut2
        val_dict['iut3'] = iut3
        val_dict['iut4'] = iut4
        val_dict['todo'] = todo
        val_dict['not_to_do'] = not_to_do

        date = datetime.datetime.strptime(date, "%Y-%m-%d")

        empty_entry = len(thoughts) == 0 and len(iut1) == 0 and len(iut2) == 0 and len(iut4) == 0 and len(todo) == 0 and len(not_to_do) == 0

        morning = morning_entry.objects.filter(date=date, user_id=request.user)

        if empty_entry:
            return HttpResponseRedirect('/morn_redirect/')
        elif len(morning) == 0:
            val_dict['last_updated'] = datetime.datetime.now().strftime("%d %B, %Y  %I:%M %p")
            json_val = json.dumps(val_dict)
            print('does not exist')
            encrypted = cryptocode.encrypt(json_val, request.user.username+str(request.user.id))
            morning_entry(date=date, user_id=request.user, data=encrypted).save()
            print('saved')
            return HttpResponseRedirect('/morn_redirect/')
        else:
            val_dict['last_updated'] = datetime.datetime.now().strftime("%d %B, %Y  %I:%M %p")
            json_val = json.dumps(val_dict)
            encrypted = cryptocode.encrypt(json_val, request.user.username+str(request.user.id))
            morning[0].data = encrypted
            morning[0].save()
            print('modified')
            return HttpResponseRedirect('/morn_redirect/')

    return render(request, 'wisely/morning.html', context={'max_date': max_date})


@login_required(login_url='/register/login/')
def morning_ajax(request):
    dt_dict = json.loads(request.POST['dt'])
    date = dt_dict['dt']
    print(date)
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    morning = morning_entry.objects.filter(date=date, user_id=request.user)
    val_dict = {
        'thoughts': '',
        'iut1': '',
        'iut2': '',
        'iut3': '',
        'iut4': '',
        'todo': '',
        'not_to_do': ''
    }
    if len(morning) == 0:
        print('does not exist')
        prev_morning = morning_entry.objects.filter(user_id=request.user)
        if len(prev_morning) == 0:
            return JsonResponse({'status': 0, 'val_dict': val_dict, 'prev': 0})
        else:
            prev_date = max(obj.date for obj in prev_morning)
            print(prev_date)
            if prev_date > date.date():
                return JsonResponse({'status': 0, 'val_dict': val_dict, 'prev': 0})
            prev_data = morning_entry.objects.filter(user_id=request.user, date=prev_date)[0].data
            prev_data = cryptocode.decrypt(prev_data, request.user.username+str(request.user.id))
            print(prev_data)
            prev_data = json.loads(prev_data)
            return JsonResponse({'status': 0, 'val_dict': val_dict, 'prev': 1, 'prev_data': prev_data, 'prev_date': prev_date})
    else:
        encrypted = morning[0].data
        val_dict = cryptocode.decrypt(encrypted, request.user.username+str(request.user.id))
        val_dict = json.loads(val_dict)
        return JsonResponse({'status': 1,
                             'val_dict': val_dict})


@login_required(login_url='/register/login/')
def morn_del_ajax(request):
    dt_dict = json.loads(request.POST['dt'])
    date = dt_dict['dt']
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    morning = morning_entry.objects.filter(date=date, user_id=request.user)
    morning[0].delete()
    return JsonResponse({'status': 1})


@login_required(login_url='/register/login/')
def evening_view(request):
    max_date = datetime.date.today()
    max_date = max_date.strftime("%Y-%m-%d")
    if request.method == "POST":

        date = request.POST['date']

        d_dx = request.POST['d_dx']
        good_things = request.POST['good_things']
        shouldnt_have_done = request.POST['shouldnt_have_done']
        modifications = request.POST['modifications']
        habits_to_let_go_of = request.POST['habits_to_let_go_of']
        strengths = request.POST['strengths']
        weaknesses = request.POST['weaknesses']
        overview = request.POST['overview']
        rating = request.POST['rating']

        value_dict = dict()

        value_dict['d_dx'] = d_dx
        value_dict['good_things'] = good_things
        value_dict['shouldnt_have_done'] = shouldnt_have_done
        value_dict['modifications'] = modifications
        value_dict['habits_to_let_go_of'] = habits_to_let_go_of
        value_dict['strengths'] = strengths
        value_dict['weaknesses'] = weaknesses
        value_dict['overview'] = overview
        value_dict['rating'] = rating

        date = datetime.datetime.strptime(date, "%Y-%m-%d")

        empty_entry = len(d_dx) == 0 and len(good_things) == 0 and len(shouldnt_have_done) == 0 and len(modifications) == 0 and len(habits_to_let_go_of) == 0 and len(strengths) == 0 and len(weaknesses) == 0 and len(overview) == 0 and rating == '-1'

        evening = evening_entry.objects.filter(date=date, user_id=request.user)

        if empty_entry:
            pass
        elif len(evening) == 0:
            value_dict['last_updated'] = datetime.datetime.now().strftime("%d %B, %Y  %I:%M %p")
            json_val = json.dumps(value_dict)
            encrypted = cryptocode.encrypt(json_val, request.user.username+str(request.user.id))
            evening_entry(date=date, user_id=request.user, data=encrypted).save()
        else:
            value_dict['last_updated'] = datetime.datetime.now().strftime("%d %B, %Y  %I:%M %p")
            json_val = json.dumps(value_dict)
            encrypted = cryptocode.encrypt(json_val, request.user.username+str(request.user.id))
            evening[0].data = encrypted
            evening[0].save()
        return HttpResponseRedirect('/')

    return render(request, 'wisely/evening.html', context={'max_date': max_date})


@login_required(login_url='/register/login/')
def evening_ajax(request):
    dt_dict = json.loads(request.POST['dt'])
    date = dt_dict['dt']
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    evening = evening_entry.objects.filter(date=date, user_id=request.user)
    if len(evening) == 0:
        return JsonResponse({'status': 0})
    else:
        encrypted = evening[0].data
        val_dict = cryptocode.decrypt(encrypted, request.user.username+str(request.user.id))
        val_dict = json.loads(val_dict)
        return JsonResponse({'status': 1, 'val_dict': val_dict})


@login_required(login_url='/register/login/')
def even_del_ajax(request):
    dt_dict = json.loads(request.POST['dt'])
    date = dt_dict['dt']
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    evening = evening_entry.objects.filter(date=date, user_id=request.user)
    evening[0].delete()
    return JsonResponse({'status': 1})


def morn_redirect(request):
    return HttpResponseRedirect('/morning/')


@login_required(login_url='/register/login/')
def anchor_view(request):
    if request.method == "POST":
        anchor_data = request.POST['anchor']
        anchor_data = cryptocode.encrypt(anchor_data, request.user.username+str(request.user.id))
        anchor(user_id=request.user, data=anchor_data).save()
        return HttpResponseRedirect('/anchor/')
    anchor_list = anchor.objects.filter(user_id=request.user)
    for i in anchor_list:
        data = i.data
        data = cryptocode.decrypt(data, request.user.username+str(request.user.id))
        i.data = data
    return render(request, 'wisely/anchor.html', context={'anchor_list': anchor_list})


def anchor_del_view(request):
    if request.method == "POST":
        anchor_id = request.POST['anchor_id']
        anchor_id = int(anchor_id)
        anchor.objects.get(id=anchor_id).delete()
        return JsonResponse({'status': 1})


def anchor_update_view(request):
    if request.method == "POST":
        anchor_id = request.POST['anchor_id']
        new_data = request.POST['new_data']
        anchor_id = int(anchor_id)
        if len(new_data) == 0:
            anchor.objects.get(id=anchor_id).delete()
        else:
            anchor_obj = anchor.objects.get(id=anchor_id)
            new_data = cryptocode.encrypt(new_data, request.user.username+str(request.user.id))
            anchor_obj.data = new_data
            anchor_obj.save()
        return JsonResponse({'status': 1})