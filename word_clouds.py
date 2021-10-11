import string
from collections import Counter
from html_functions import make_HTML_word, make_HTML_box, print_HTML_file

def getInputFile():
    print('Program untuk membuat word cloud dari text file')
    print('----------------------------------------------')
    print('hasilnya disimpan sebagai file html,')
    print('yang bisa ditampilkan di browser')
    return input('\n\nSilakan masukkan nama file untuk speech: ')

def getInputStopWords():
    return input('Silakan masukkan nama file untuk stop words: ')

def getListStopWords(file_stopwords):
    stop_words = open('stopwords/' + file_stopwords, 'r')
    return stop_words.read().split()

def getListSpeech(file_input):
    file_speech = open('speeches/' + file_input, 'r')
    removed_punctuation = file_speech.read().translate(str.maketrans('', '', string.punctuation))
    return removed_punctuation.lower().split()

def doRemoveWords(list_speech, list_stopwords):
    filtered_list_speech = [];
    for list in list_speech:
        if list not in list_stopwords:
            filtered_list_speech.append(list)

    counted_filtered_list_speech = Counter(filtered_list_speech)
    return counted_filtered_list_speech.most_common(56)

def doPrintTableAndMakeHTML(final_list):
    value_list = []
    length_final_list = len(final_list)
    for i in range(length_final_list):
        value_list.append(final_list[i][1])
        if i != 0 and i % 4 == 0:
            print(f'\n{final_list[i][1]: <2} : {final_list[i][0]: <15}', end = " ")
        else:
            print(f'{final_list[i][1]: <2} : {final_list[i][0]: <15}', end = " ")
    final_list = sorted(final_list)
    body = ''
    for i in range(length_final_list):
        body += "\n" + make_HTML_word(final_list[i][0], final_list[i][1], max(value_list), min(value_list))
    body_string = make_HTML_box(body)
    print_HTML_file(body_string, file_input)

def main():
    global file_input
    file_input = getInputFile()
    file_stopwords = getInputStopWords()
    list_stopwords = getListStopWords(file_stopwords)
    list_speech = getListSpeech(file_input)
    final_list = doRemoveWords(list_speech, list_stopwords)
    doPrintTableAndMakeHTML(final_list)

main()