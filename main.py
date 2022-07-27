# quizzing!
score = 0

print("""I am going to test your intelligence
I have a series of 4 questions which never change
Please answer to the best of your ability

Let us start
""")
answers1 = ["yes", "yessir", "absolutely", "for sure", "yes sir", "fosho"]
answers2 = ["european", "euro'peeing'", "euro-peeing", "euro-pean"]
answers3 = ["water", "coke", "coca-cola", "cola", "coke the liquid kind", "cocacola"]
answers4 = ["red paint", "paint that is red", "red-paint", "the color red as paint", "redpaint"]

q1 = input("Question 1: Does Ryan Reynolds have a beautiful smile? ").lower()
print("that was not a matter of opinion btw")
for i in answers1:
    if q1 == i:
        score += 1
q2 = input("Question 2: If you are Russian while you go towards the washroom, inside the washroom you are? ").lower()
print("well hopefully you know how to spell")
for i in answers2:
    if q2 == i:
        score += 1
q3 = input("Question 3: What is a more refreshing beverage, pepsi or coca-cola? ").lower()
print("yeah im very creative")
for i in answers3:
    if q3 == i:
        score += 1
q4 =  input("Question 4: What is red and smells like blue paint? ").lower()
print("this one is tricky, my guess would be apples covered in blue paint")
for i in answers4:
    if q4 == i:
        score += 1

percentile = score/4 * 100
typedpercentilescore = "(" + str(percentile) + "%" + ")"

print("YOUR RESULTS:")
print(score,"/ 4", typedpercentilescore)
print("good job i guess")