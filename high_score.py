num_scores = int(input("enter the no.of scores  "))
score_list = []
for i in range(0,num_scores):
    scores = int(input("enter score  "))
    score_list.append(scores)
print(score_list)
high_score=0
for n in score_list:
    n>high_score
    high_score=n
print(high_score)