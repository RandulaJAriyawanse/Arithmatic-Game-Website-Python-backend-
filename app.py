from flask import Flask, render_template, request

import random

app = Flask(__name__)

operators = ["+", "-", "*", "/"]


@app.route('/', methods=['GET'])
def index():
    for all in range(1):
        i = random.choice(operators)
        if i == "+": 
            int_a_1 = random.randint(1, 150)
            int_a_2 = random.randint(1, 100)
            operator = "+"
            question = str(int_a_1) + i + str(int_a_2)
        elif i == "-":
            operator_s = "-"
            int_s_1 = random.randint(2, 150)
            int_s_2 = random.randint(1, int_s_1)
            question = str(int_s_1) + i + str(int_s_2)
        elif i == "*":
            int_m_1 = random.randint(1, 12)
            int_m_2 = random.randint(1, 12)
            operator_m = "*"
            question = str(int_m_1) + i + str(int_m_2)
        elif i == "/":
            operator_d = "/"
            int_d_1 = random.randint(2, 500)
            factors = []
            for p in  range(2, int_d_1+1):
                if int_d_1%p == 0: 
                    factors.append(str(p))
            if len(factors) == 1: 
                continue
            question = str(int_d_1) + i + str(random.choice(factors[:-1]))

    return render_template('index.html', ques=question)

@app.route('/submit-answer', methods=['POST'])
def submitAnswer():
    answer = request.form['a']
    question = request.form['q']
    currentQuestionNo = int(request.form['n'])
    

    print("input is " , answer)
    print("question is " , question)
    print("answer is ", str(int(eval(question))))

    for all in range(1):
        i = random.choice(operators)
        if i == "+": 
            int_a_1 = random.randint(1, 150)
            int_a_2 = random.randint(1, 100)
            operator = "+"
            next_ques = str(int_a_1) + i + str(int_a_2)
        elif i == "-":
            operator_s = "-"
            int_s_1 = random.randint(2, 150)
            int_s_2 = random.randint(1, int_s_1)
            next_ques = str(int_s_1) + i + str(int_s_2)
        elif i == "*":
            int_m_1 = random.randint(1, 12)
            int_m_2 = random.randint(1, 12)
            operator_m = "*"
            next_ques = str(int_m_1) + i + str(int_m_2)
        elif i == "/":
            operator_d = "/"
            int_d_1 = random.randint(2, 250)
            factors = []
            for p in  range(2, int_d_1+1):
                if int_d_1%p == 0: 
                    factors.append(str(p))
            if len(factors) == 1: 
                continue
            next_ques = str(int_d_1) + i + str(random.choice(factors[:-1]))
    

    if answer == str(int(eval(question))) : 
        return {
            'res': "Correct", 
            'next_question' : next_ques, 
            'question_no' : currentQuestionNo + 1,
        }
    else : 
        return  {
            'res': "You were wrong , please try new question now ", 
            'next_question' : question, 
            'question_no' : currentQuestionNo,
        }

if __name__ == "__main__":
    app.run(debug=True)


