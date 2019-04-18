from django.shortcuts import render
from .models import TextEmoji 
import requests
import json
from .emo_utils import read_glove_vecs
from .forms import MsgInputForm, MsgOutputForm

# Just Need To Add  A View 


def text_to_sentence(text):

    start = 0
    sentences = []
    for i in range(len(text)):
        if text[i] == '.':
            sentence = text[start:(i)]
            start = i + 2
            sentences.append(sentence)
    if not sentences:
        sentences.append(text)
    return sentences


def emojify(text):

    url = 'http://0.0.0.0:5000/emojify/api/v1.0'
    data = {}
    word_to_index, index_to_word, word_to_vec_map = read_glove_vecs('glove.6B.50d.txt')
    i = 0

    # List of sentences to emojify
    sentences = text_to_sentence(text)
    
    # Creating Json Object
    for s in sentences:
        data[str(i)] = s
        i += 1
    data['word_to_index'] = word_to_index
    j_data = json.dumps(data)

    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)

    print(r.text)
    json_data = json.loads(r.text)
    print(json_data)

    # Just Need To concatinate all values in json object and add periods
    out = ""
    for (k, v) in json_data.items():
        out += str(v) + '. ' 
    
    return out


def emojitext(request):

    # Form
    if request.method == 'POST':
        form = MsgInputForm(request.POST)
        output_form = MsgOutputForm()
        print (form.errors)
        print (output_form.errors)
        print("valid")
        text = form.cleaned_data.get('text')
        emojify_text = emojify(text)
        print(emojify_text)
        return render(request, 'emojify/index.html', {'form' : form, 'emoji_text': emojify_text})
    else:
        form = MsgInputForm()
        output_form = MsgOutputForm()
    return render(request, 'emojify/index.html', {'form' : form})