from datetime import datetime

question_collection = ""
x = 0
update_value = 0
list_of_questions={}
date = datetime.now().strftime("%Y_%m_%d")
while x == 0:
    choice = input("Enter \"question\" or \"upvote\": ")
    if choice == "question":
        key = input("Enter a question:  ")
        value = 1
        list_of_questions[key]= value
        print(list_of_questions)
    elif choice == "upvote":
        print(list_of_questions)
        upvote_question = input("Which question do you want to upvote:  ")
        list_of_questions[upvote_question] = list_of_questions[upvote_question] + 1
    else:
        print("invalid input!")
    
    end_of_lec = input("Has the lecture ended and question/answer period began, enter \"yes\" or \"no\": ")
    if end_of_lec == "yes":
        x = 1
        file = open("Questions_on" + date + '.txt', "w")
        file.write("list of questions : " + "\n" + question_collection + "\n")
        file.close()


num_addressed_questions = len(list_of_questions.keys())
answer_reviews = []

print("\nQuestion list: ")
for key, value in sorted(list_of_questions.items(), key=lambda kv: kv[1], reverse=True):
        question_collection = question_collection + "%s: %s" % (key, value) + "\n"
        print(question_collection)

for i in range(num_addressed_questions):
    rate_answer = input("Rate the answers to the questions shown above in the order it is presented.\nEnter a 1 if the answer needs further clarification. Enter a 2 if the answer is satisfactory. Enter a 3 if the question was skipped: ")
    answer_reviews.append(rate_answer)
    print(answer_reviews)

answer_file = open("Answer_on" + date, "w")
for element in answer_reviews:
    answer_file.write(element + "\n")
answer_file.close()

