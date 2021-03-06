from datetime import datetime

question_collection = ""
x = 0
update_value = 0
list_of_questions={}
date = datetime.now().strftime("%Y_%m_%d")

student_number = input("Enter your student number so your professor can identify you:   ")
while x == 0:
    choice = input("Enter \"question\" or \"upvote\":   ")
    print("\n")
    if choice == "question":
        key = input("Enter a question:  ")
        value = 1
        list_of_questions[key]= value
        print(list_of_questions)
        print("\n")
    elif choice == "upvote":
        upvote_question = input("Which question do you want to upvote:  ")
        list_of_questions[upvote_question] = list_of_questions[upvote_question] + 1
        for key, value in sorted(list_of_questions.items(), key=lambda kv: kv[1], reverse=True):
            question_collection = question_collection + "%s: %s" % (key, value) + "\n"
        print("\n")
    else:
        print("invalid input! \n")
    end_of_lec = input("Has the lecture ended and question/answer period began, enter \"yes\" or \"no\": ")
    print("--------------------------------------------------------------------------------------------------------")
    if end_of_lec == "yes":
        x = 1
        file = open("Questions_on" + date + '.txt', "w")
        file.write("list of questions : " + "\n" + question_collection + "\n")
        file.close()


num_addressed_questions = len(list_of_questions.keys())
answer_reviews = []

for i in range(num_addressed_questions):
    print("\n")
    print("Currently answering the following question:   ")
    print(list(list_of_questions.items())[i])
    print("\n")
    rate_answer = input("Rate the answers to the questions shown above in the order it is presented.\nEnter a 1 if the answer needs further clarification. Enter a 2 if the answer is satisfactory. Enter a 3 if the question was skipped: ")
    answer_reviews.append(rate_answer)
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

answer_file = open("Answer_on" + date, "w")
for element in answer_reviews:
    answer_file.write(element + "\n")
answer_file.close()

