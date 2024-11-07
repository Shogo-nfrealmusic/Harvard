# scores = [72, 73, 33]

# average = sum(scores) / len(scores)

# print(f"The average score is {average}")

scores = []
for i in range(3):
    score = int(input("Enter a score: "))
    scores.append(score)
    
average = sum(scores) / len(scores)
print(f"The average score is {average}")    