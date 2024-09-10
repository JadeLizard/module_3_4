def single_root_words(root_word, *other_words): #задаю слово + кортеж из хз скольких слов
    same_words = [] #скписок куда будем все подходящее вносить
    for i in other_words: #для каждого слова из кортежа где хз сколько слов
        if root_word.lower() in i.lower() or i.lower() in root_word.lower(): #если с маленькой буквы слово есть в слове из списка, или слово из списка есть в слове, то
            same_words.append(i) #добавляем в список который сделали ранее для этого
    return same_words #когда проверили все слова подтягиваем сюда все что в том списке образовалось
result = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies') #список 1
print(result)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel') #список 2
print(result2)
