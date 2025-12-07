#Isaiah Wolf 3/21/24
#IsaiahProgram4

TESTS = 7

total = 0.0
average = 0.0
grades = []

for i in range(1, TESTS + 1):
    score = float(input(f"Score {i}: "))
    grades.append(score)
    total += score

average = total / TESTS

print("\nScore \t\t\t Numeric Score")
for i, score in enumerate(grades):
    print(f"Score {i + 1}: \t\t\t {score:.1f}")
print(f"Total: \t\t\t\t {total:.1f}")
print(f"Average Score: \t\t\t {average:.1f}")
