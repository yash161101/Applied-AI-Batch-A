import pulp

def define_problem():
    # Initialize the problem
    prob = pulp.LpProblem("IPL_Team_Selection", pulp.LpMaximize)

    # Define decision variables
    x = pulp.LpVariable.dicts("Player", range(1, 21), cat='Binary')

    # Objective function
    prob += (95*x[1] + 90*x[2] + 85*x[3] + 92*x[4] + 88*x[5] + 86*x[6] +
             94*x[7] + 87*x[8] + 89*x[9] + 88*x[10] + 90*x[11] + 91*x[12] +
             88*x[13] + 87*x[14] + 89*x[15] + 90*x[16] + 85*x[17] + 86*x[18] +
             84*x[19] + 87*x[20]), "Total Performance Score"

    # Constraints
    prob += (16*x[1] + 15*x[2] + 12*x[3] + 14*x[4] + 13*x[5] + 11*x[6] +
             15*x[7] + 10*x[8] + 12*x[9] + 11*x[10] + 14*x[11] + 13*x[12] +
             12*x[13] + 11*x[14] + 12*x[15] + 14*x[16] + 10*x[17] + 11*x[18] +
             9*x[19] + 11*x[20]) <= 140, "Budget Constraint"

    prob += (x[1] + x[2] + x[3] + x[4] + x[14] + x[15]) >= 4, "Batsmen Constraint"
    prob += (x[7] + x[8] + x[9] + x[10] + x[17] + x[18] + x[19]) >= 3, "Bowlers Constraint"
    prob += (x[5] + x[6] + x[16]) >= 1, "Wicketkeeper Constraint"
    prob += (x[11] + x[12] + x[13] + x[20]) >= 2, "Allrounders Constraint"
    prob += (x[3] + x[4] + x[6] + x[8] + x[9] + x[12] + x[18] + x[20]) <= 4, "Overseas Constraint"
    prob += (x[1] + x[2] + x[5] + x[7] + x[10] + x[11] + x[13] + x[14] + x[15] + x[16] + x[17] + x[19]) >= 7, "Indian Players Constraint"
    prob += sum(x[i] for i in range(1, 21)) == 11, "Total Players Constraint"

    return prob, x

def solve_problem(prob, x):
    # Solve the problem
    prob.solve()

    # Extract selected players
    selected_team = []
    for i in range(1, 21):
        if x[i].varValue == 1:
            selected_team.append(i)

    return selected_team

def get_selected_team_names(selected_team):
    selected_team_names = ["Virat Kohli", "Rohit Sharma", "Kane Williamson", "AB de Villiers",
                           "KL Rahul", "Jos Buttler", "Jasprit Bumrah", "Pat Cummins", "Kagiso Rabada",
                           "Bhuvneshwar Kumar", "Hardik Pandya", "Ben Stokes", "Ravindra Jadeja", 
                           "Shikhar Dhawan", "Suryakumar Yadav", "Rishabh Pant", "Mohammed Shami", 
                           "Trent Boult", "Yuzvendra Chahal", "Marcus Stoinis"]

    selected_team_final = [selected_team_names[i-1] for i in selected_team]
    return selected_team_final

def main():
    # Define the problem
    prob, x = define_problem()

    # Solve the problem
    selected_team = solve_problem(prob, x)

    # Get selected team names
    selected_team_final = get_selected_team_names(selected_team)

    # Display the selected team
    print("Selected IPL Team:")
    for player in selected_team_final:
        print(player)

if __name__ == "__main__":
    main()
