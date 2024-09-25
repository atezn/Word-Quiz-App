import sys,random,json

with open('words.json', 'r', encoding='utf-8') as words:
    dictionary = json.load(words)

#random word selector
def word_selector():
        with open('done.json', 'r', encoding='utf-8') as done_file:
            with open('review.json', 'r', encoding='utf-8') as done_review:
            
                done_words = set(json.load(done_file)) | set(json.load(done_review))
                #checking the available, not done words
                available_words = set(dictionary.keys()) - done_words
                if not available_words :  #if there is none available words, then we are done with the list
                    return 'Tum kelimeler tamamlandi'
                
                while True: #if there is available words in the list, then we proceed to check if the word that we choose in the done_list, if so we choose again
                    random_word = random.choice(list(available_words))
                    if random_word not in done_words:
                        meaning = dictionary[random_word]
                        return random_word, meaning

last_selected_word = None
def review_word_selector():
    global last_selected_word
    with open('review.json', 'r', encoding='utf-8') as reviewList:   
        review_words = set(json.load(reviewList))
        if not review_words:
            return False
        
        if len(review_words) == 1:
            word = list(review_words)[0]
            last_selected_word = word
            return word, dictionary[word]

        #if last selected word exists remove it from reviw_words, if not available words are just all of the review_words
        available_words = review_words - {last_selected_word} if last_selected_word else review_words
        
        random_review_word = random.choice(list(available_words))
        meaning = dictionary[random_review_word]
        last_selected_word = random_review_word
        
        return random_review_word, meaning
        

def review_choice_generator():
    choices = []
    choices.append(random.choice(list(dictionary.values())))
    
     
    temp = review_word_selector()
    if temp:
        word, meaning = temp[0], temp[1]

        choices.append(meaning)
        random.shuffle(choices)
        choices.append(word)
        return choices,meaning


def review_editWord():
    with open('review.json', 'r') as review_words:
        return sorted(json.load(review_words))


def editWordRemove(word):
    with open('review.json', 'r') as file:
        review_list = json.load(file)
    
    try:
        with open('done.json', 'r') as file:
            done_list = json.load(file)
    except FileNotFoundError:
        done_list = []  
    
    if word in review_list:
        review_list.remove(word)
        done_list.append(word)


    with open('review.json', 'w') as file:
        json.dump(review_list, file, indent=2)
    
    with open('done.json', 'w') as file:
        json.dump(done_list, file, indent=2)

def editWordCheck(word):
    with open('review.json', 'r') as file:
        review_list = json.load(file)
    
    try:
        with open('done.json', 'r') as file:
            done_list = json.load(file)
    except FileNotFoundError:
        done_list = []

    if word in done_list:
        done_list.remove(word)
        review_list.append(word)

    with open('review.json', 'w') as file:
        json.dump(review_list, file, indent=2)
    
    with open('done.json', 'w') as file:
        json.dump(done_list, file, indent=2)


#choice generator
def choice_generator():  
    choices = []
    for _ in range(3):
        choices.append(random.choice(list(dictionary.values())))
    
    temp = word_selector()
    word_, mean = temp[0], temp[1]
    choices.append(mean)
    random.shuffle(choices)
    choices.append(word_)
    return choices,mean
 

#checking the answer
def checker(word,user,answer):
    #add word to done list if guessed correctly
    if user == answer:
        with open('done.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            data.append(word)
            with open('done.json', 'w', encoding='utf-8') as write:    
                json.dump(data, write, ensure_ascii=False)
        return True
    #add word to review list if guessed incorrectly
    else:
        with open('review.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            data.append(word)
            with open('review.json', 'w', encoding='utf-8') as write:    
                json.dump(data, write, ensure_ascii=False)
        return False

