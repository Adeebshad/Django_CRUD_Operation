from django.http import JsonResponse
from .helper import responseFormat
from .models import Values
from .error_codes import RequestError, DatabaseError
from django.views.decorators.csrf import csrf_exempt
import json

def values(request):
    return JsonResponse(responseFormat(
        success = True,
        message = "The request is successful",
        data = {
            'value' : [ value.serialize() for value in Values.objects.all() if value.publish]
        },
        errors = []
    ))

@csrf_exempt
def addValue(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(responseFormat(
                success = False,
                message = "This type of data can be decoded",
                data = {},
                errors = [RequestError.INVALID_REQUEST_FORMAT]
            ))
        
        value = Values.objects.create(
            name = data.get('name', 'atik'),
            detail = data.get('detail', 'china'),
            publish = data.get('publish', False)
        )

        return JsonResponse(responseFormat(
            success = True,
            message = f'The requested data is added.The resquested methos is {request.method}.',
            data = value.serialize(),
            errors = []
        ))

    else:
        return JsonResponse(responseFormat(
            success = False,
            message = f'The resquested methos {request.method} is not right',
            data = {},
            errors = [RequestError.METHOD_NOT_ALLOWED]
        ))

@csrf_exempt
def updateValue(request, id):
    if request.method == 'POST':
        try:
            value = Values.objects.get(pk=id)
        except Values.DoesNotExist:
            return JsonResponse(responseFormat(
                success = False,
                message = "This id does not have any data on database.",
                data = {},
                errors = [DatabaseError.DATA_ERROR]
            ))

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(responseFormat(
                success = False,
                message = "This type of data can be decoded.",
                data = {},
                errors = [RequestError.INVALID_REQUEST_FORMAT]
            ))
        
        
        value.name = data.get('name', 'atik')
        value.detail = data.get('detail', 'china')
        value.publish = data.get('publish', False)
        value.save()

        return JsonResponse(responseFormat(
            success = True,
            message = f'Id {id} data is updated .The resquested methos is {request.method}',
            data = value.serialize(),
            errors = []
        ))

    else:
        return JsonResponse(responseFormat(
            success = False,
            message = f'The resquested methos {request.method} is not right',
            data = {},
            errors = [RequestError.METHOD_NOT_ALLOWED]
        ))

@csrf_exempt
def deleteValue(request,id):
    if request.method == 'POST':
        try:
            value = Values.objects.get(pk = id)
        except IdDoesNotexit:
            return JsonResponse(responseFormat(
                success = False,
                message = "This {id} does not have any data on database.",
                data = {},
                errors = [DatabaseError.DATA_ERROR]
            ))

        else:
            value.delete()

        return JsonResponse(responseFormat(
            success = True,
            message = f'Succefully deleted id {id}. Requested Method is {request.method}',
            data = value.serialize(),
            errors = []
        ))
    
    else:
        return JsonResponse(responseFormat(
            success = False,
            message = f'Requested Method {request.method} is not right',
            data = {},
            errors = [RequestError.METHOD_NOT_ALLOWED]
        ))
