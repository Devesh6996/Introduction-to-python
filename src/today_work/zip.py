answers = ["b", "a", "d", "c"]
correct = ["b", "c", "d", "c"]
score = 0
for compare in zip(answers, correct):
    if compare[0] == compare[1]:
        score += 1
print(f"Score: {score}/4")