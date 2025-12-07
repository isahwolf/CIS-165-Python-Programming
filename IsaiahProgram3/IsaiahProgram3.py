#Isaiah Wolf 3/17/24
#IsaiahProgram3

score1 = 0.00
score2 = 0.00
score3 = 0.00
score4 = 0.00
score5 = 0.00
average = 0.00

def main():
    score1 = float(input('Enter the first score: '))
    score2 = float(input('Enter the second score: '))
    score3 = float(input('Enter the third score: '))
    score4 = float(input('Enter the fourth score: '))
    score5 = float(input('Enter the fifth score: '))
    
    average = calc_avg(score1, score2, score3, score4, score5)

    print("\nScore\t\tNumeric Score\t\tLetter Grade")
    print("Score 1:\t", score1, "\t\t\t", get_grade(score1))
    print("Score 2:\t", score2, "\t\t\t", get_grade(score2))
    print("Score 3:\t", score3, "\t\t\t", get_grade(score3))
    print("Score 4:\t", score4, "\t\t\t", get_grade(score4))
    print("Score 5:\t", score5, "\t\t\t", get_grade(score5))
    print("\nAverage Score:\t", average)

def calc_avg(score1, score2, score3, score4, score5):
    average =(score1 + score2 + score3 + score4 + score5)/5
    return average


def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
main()
