#quizz app

print("You will be provided with questions one by one. Input option A,B,C or D. Score will be displayed at the end")

questions = ["Question", "Question", "Question", "Question", "Question", "Question", "Question", "Question"]
answers = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
i = 0
size = len(questions)
ans_input = ['Nil']*size
#print(ans_input)
for i in range(0, size):
    print(questions[i])
    print("answer:")
    ans_input[i] = input()

flag = 0
for i in range(0, size):
    if ans_input[i] == answers[i]:
        flag = flag + 4
        print(i+1, '   +4')
    else:
        flag = flag - 1
        print(i+1, '   -1')
print("score: ", flag)

