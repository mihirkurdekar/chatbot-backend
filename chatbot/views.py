import json

from django.http import HttpResponse, JsonResponse

from .serializers import FileUploadForm,TrainingObjectSerializer
from django.views.decorators.csrf import csrf_exempt

from .utils.conversation_format_util import formatUserInput
from .utils.csv_handler import csvToJson
from .utils.conversation_answer_util import getAnswer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def index(request):
    return HttpResponse('Hello World')


@csrf_exempt
@api_view(['POST'])
def upload_file(request):
    form = FileUploadForm(request.POST,request.FILES)
    if form.is_valid():
        file = request.FILES['file']
        return JsonResponse(csvToJson(file),safe=False)
    else:
        return HttpResponse('invalid',status=400)

@csrf_exempt
@api_view(['PUT'])
def train(request):
    serializer = TrainingObjectSerializer(data=json.loads(request.body),many=True)
    if serializer.is_valid():
        data = formatUserInput(serializer.data)
        return JsonResponse(data,safe=False)
    else:
        return HttpResponse('invalid', status=400)

@csrf_exempt
@api_view(['GET'])
def execute(request):
    question = request.GET.get('question',None)
    return JsonResponse(getAnswer(question),safe=False)