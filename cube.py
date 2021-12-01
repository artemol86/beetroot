six_edges_cube = range(1,7)
twelve_edges_cube = range(1,13)
twenty_edges_cube = range(1,21)
experiments = [2, 11, 3, 5, 3, None, 1, 9, 9, 8, 12, 7, 4, None, 6, 2, 1, 3, 8, 3, 12, 4, 6, None, 11, 2, 5, 7, 3, 9]
experiments = [item for item in experiments if item != None]
valid_experiments_set = set(experiments)

if max(valid_experiments_set) <= 6:
    edges = six_edges_cube
    print("This is six edges cube\n")
elif 6 <= max(valid_experiments_set) <= 12:
    edges = twelve_edges_cube
    print("This is twelve edges cube\n")
elif 12 <= max(valid_experiments_set) <= 20:
    edges = twenty_edges_cube
    print("This is twenty edges cube\n")
else:
    print("Your code is incorrect, please double check it")

for edge in edges:
    probability = experiments.count(edge) / len(experiments)
    print(f"Probability for edge {edge} is {probability}")