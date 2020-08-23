from .conversation_format_util import conversation
import requests

def getAnswer(question):
    res = requests.get('http://localhost:5000/parse',
                 params={'model':'default','project':'default','q':question})
    if res.status_code != 200:
        raise OverflowError(res.json())
    else:
        intent = res.json()['intent']['name']
        if not intent:
            intent='None'
        return conversation[intent]
