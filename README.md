# WORD QUIZ APP
    #### #### Video Demo: https://youtu.be/rTMc2Tuew8Q
    #### Description: This project is an example of a really simple word quiz app made with Python-PyQt5. The main purpose of the app is to help users expand their vocabulary in a desired language. The default version is set to translate from English to Turkish, but you can manually change the word set to fit your learning goals.

## Features:

   * Quiz Mode: The app generates random words from a predefined word list, presenting multiple-choice questions.  Users select the correct translation or choose the "I don't know" option. After each answer, the correct translation is displayed.
   
   * Streak System: Tracks the number of consecutive correct answers to encourage progress.
   
   * Review Mode: Incorrectly answered words are stored in a review list, allowing users to focus on problem areas.
   
   * Editable Word List: Users can edit the review list, marking words as learned or keeping them for further practice.


## Installation:

   * Ensure you have Python 3.x and PyQt5 installed.
   * Clone the project
   * Run the app with --> "python project.py" from terminal or anyway you can.

##  Usage:

   * Starting the Quiz: Upon launching, the app displays a word and multiple translation options. Select the correct translation or the 'I don't know' option to progress.
    
   * Review Mode: You can access words you've struggled with by clicking "Review Words." The app will quiz you again on these words.
    
   * Editing Review List: Use the "Edit Words" feature to manage your review list.
      
## Confugiration:
   
   * words.json: This is the main source of words and their meanings. It contains a dictionary where the keys represent words, and the values represent their meanings. By default, the words.json file contains English words as keys and Turkish translations as values. You can manually adjust this file to suit your learning needs, as long as the key-value pairs are properly formatted. You may use tools like ChatGPT to assist with this process.
   
   * done.json: This file stores a list of words that you have guessed correctly during the quiz. You can manually adjust this file (e.g., remove words), and the app will present those words to you again.

   * review.json: This file contains words that you either guessed incorrectly or selected the "I don't know" option. You can manually adjust this file as well(remove), and the app will present those words again. Or you can use the "Edit Words" feature from the "Review List" section within the app to uncheck words. This automatically moves them to the done.json file.
