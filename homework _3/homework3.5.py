from random import sample

def input_valid_difficulty(prompt=''):
    while True:
        try:
            n = int(input(prompt))
            if n < 0 or n > 3:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice! Enter 1,2 or 3.")
            prompt = "Select a difficulty?: (0 to exit):"
    return n


difficulty = input_valid_difficulty ("Select a difficulty?: (0 to exit):")
if difficulty == 0:
    quit()
elif difficulty == 1:
    print("Easy mode selected!")
    lives, max_num, questions = 3, 10, 5
elif difficulty == 2:
    print("Medium mode selected!")
    lives, max_num, questions = 2, 25, 10
elif difficulty == 3:
    print("Hard mode selected!")
    lives, max_num, questions = 1, 50, 15


operations = ['+', '-']  
all_q_and_a = []
for i in range(20):
  for j in range(20):
    for op in operations:
      all_q_and_a.append((f"{i} {op} {j} = ?: ", eval(f"{i} {op} {j}")))

chosen_q_and_a = sample(all_q_and_a, questions)
score = 0
for q in chosen_q_and_a:
  if lives == 0:
    break
  while lives > 0:
    answer = int(input(q[0]))
    if answer == q[1]:
      print("Correct")
      score += max_num 
                        
                      
      break
    else:
      lives -= 1
      print("Sorry, try again")

print(f"Your score was {score}")