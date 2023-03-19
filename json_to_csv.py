
def correspondence_counter(main_text,comment_text):
    count = 0
    for i in main_text.split():
        for j in comment_text.split():
            if i == j:
                count+=1
    return(count/len(comment_text.split()))

def sentiment_analysis(text):
    print()


import json

data_file = open('case_data', 'w',encoding = 'utf-8')
data_file.write('слова в тексте,символы в тексте,точки в тексте,запятые в тексте,восклицательные знаки в тексте,вопросительные знаки в тексте,слова в комментарии,символы в комментарии,точки в комментарии,запятые в комментарии,восклицательные знаки в комментарии,вопросительные знаки в комментарии,соответствие текста комментарию,оценка комментария\n')

with open('ranking_train.jsonl', 'r') as json_file:
    json_list = list(json_file)

for json_str in json_list:
    count = 0
    result = json.loads(json_str)
    main_text = result['text']
    main_words = len(main_text.split())
    main_symbols = len(main_text)
    main_dots = main_text.count('.')
    main_commas = main_text.count(',')
    main_question_marks = main_text.count('?')
    main_exclamation_marks = main_text.count('!')
    for i in range(0,len(result['comments'])):
        count += 1
        comment_text = result['comments'][i]['text']
        comment_score = result['comments'][i]['score']
        comment_words = len(comment_text.split())
        comment_symbols = len(comment_text)
        comment_dots = comment_text.count('.')
        comments_commas = comment_text.count(',')
        comment_question_marks = comment_text.count('?')
        comment_exclamation_marks = comment_text.count('!')
        correspondence = correspondence_counter(main_text,comment_text)
        data_file.write(str(main_words)+','+str(main_symbols)+','+str(main_dots)+','+str(main_commas)+','+str(main_exclamation_marks)+','+str(main_question_marks)+','+str(comment_words)+','+str(comment_symbols)+','+str(comment_dots)+','+str(comments_commas)+','+str(comment_exclamation_marks)+','+str(comment_question_marks)+','+str(correspondence)+','+str(comment_score)+'\n')
    print(count)
data_file.close()
