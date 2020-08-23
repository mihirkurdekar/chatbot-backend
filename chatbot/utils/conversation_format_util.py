from ..serializers import TrainingObjectSerializer
from collections import defaultdict
import requests
conversation = defaultdict(str)
def trainRasa(rasa_json):
    res = requests.post(
        'http://localhost:5000/train',
        params={'model':'default','project':'default'},
        json=rasa_json)
    if res.status_code != 200:
        raise OverflowError(res.json())
    else:
        return {'message': 'trained'}

def rasaEntity(text, word_list):
    res = []
    for word in word_list:
        res.append({
            'start': text.index(word),
            'end': text.index(word) + len(word) - 1
        })
    return res

def formatUserInput(userInput: TrainingObjectSerializer):
    global conversation
    conversation['None'] = "Didn't get you!"
    commonExamples = []
    for entry in userInput:
        conversation[entry['intent']] = entry['answer']
        commonExamples.append({
            'text' : entry['question'],
            'intent': entry['intent'],
            'entity': rasaEntity(entry['question'], entry['entities'])
        })

    return trainRasa({
        "rasa_nlu_data": {
            "common_examples": commonExamples,
            "regex_features" : [],
            "lookup_tables"  : [],
            "entity_synonyms": []
        }})