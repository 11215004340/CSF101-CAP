####################################
#Shyam Ghallay
#First Year, Instrumentation and Control Engineering
#02230225
####################################
#REFERENCES
#https://www.w3schools.com/python/python_tuples.asp
#https://www.geeksforgeeks.org/python-programming-examples/
#https://stackoverflow.com/questions/32293947/assistance-on-python-rock-paper-scissors-using-input-file?newreg=747149a1330a46c5a1699c21443093a3

################################
#SOLUTION
#YourSolutionScore: 49977
#CSF101-CAP/input_5_cap1.txt
################################

#Define a function that takes a file_path as input.
def read_game_data(file_path):
    game_rounds = []
    
    #opens the file specified by the file_path variable in read mode and assigns it to the variable named 'file'.
    #Using 'with' ensures the file is properly closed after use.
    with open(file_path, 'r') as file:
        # It iterate over each line in the file.
        for line in file:
            #It splits each line into two parts, opponent_play and outcome
            opponent_play, outcome = line.strip().split()
            #appends a tuple to the game_rounds list. Each tuple contains two elements: opponent_play and outcome.
            game_rounds.append((opponent_play, outcome))
    return game_rounds #It returns the list of game rounds.

#Define the function that takes game_rounds(list of tuples) as input
def calculate_score(game_rounds):
    #It initialize a variable to 0
    score = 0
    
    #Using if else statement, it iterates through each tuple in the list.
    for opponent_play, outcome in game_rounds:
        #checks if the opponent's play is "A", "B", or "C"
        #And calculate the score based on outcome
        if opponent_play == "A": 
            round_score = 3 if outcome == "X" else (4 if outcome == "Y" else 8)
        elif opponent_play == "B":
            round_score = 1 if outcome == "X" else (5 if outcome == "Y" else 9)
        else:
            round_score = 2 if outcome == "X" else (6 if outcome == "Y" else 7)
            
        #Add the round score to the total score
        score += round_score

    return score

#Calls the function read_game_data() and passes the string 'input_4_cap1.txt'(file) as an argument.
input_file_path = read_game_data('CSF101-CAP/input_5_cap1.txt')

# It calls the function and calculate the total score using the function and store it in 'total_score'.
total_score = calculate_score(input_file_path)

print("Total Score:",total_score)