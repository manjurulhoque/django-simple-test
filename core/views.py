from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def all_values(request):
    # if 'values' not in request.session:
    #     data = {1: "1", 2: "2"}
    #     request.session['values'] = data
    #     request.session.set_expiry(1 * 60)
    if request.method == 'GET':
        if 'values' in request.session:
            all_data = request.session['values']
        else:
            all_data = {}

        if len(request.GET.getlist('keys')) > 0:
            keys = request.GET.get('keys').split(',')
            all_data = {key: value for (key, value) in all_data.items() if key in keys}

        request.session.set_expiry(5 * 60)  # Resetting TTL
        return JsonResponse(data=all_data, status=200)
    elif request.method == 'POST':
        if 'values' in request.session:
            data = dict(request.session['values'])
            data.update(request.POST.dict())
            request.session['values'] = data
        else:
            request.session['values'] = request.POST.dict()
        request.session.set_expiry(5 * 60)
        return JsonResponse({'message': 'Successfully stored'}, status=201)
    elif request.method == 'PATCH' or request.method == 'PUT':
        if 'values' in request.session:
            data = dict(request.session['values'])
        else:
            data = dict({})

        keys = list(data.keys())
        body = request.PUT.dict()
        for k, v in body.items():
            k = str(k).strip()
            if k in keys:
                data[k] = v

        request.session['values'] = data
        request.session.set_expiry(5 * 60)
        return JsonResponse({'message': 'Successfully updated'}, status=201)
