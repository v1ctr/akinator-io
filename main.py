"""
Main Module
"""

import graph
from predicates import LessThan, Equals


if __name__ == "__main__":
    G = graph.Graph()
    G.create_variable("Befristung")
    G.create_variable("Arbeitszeit")

    g_109 = G.create_goal("109")
    g_110 = G.create_goal("110")

    LT = LessThan(7)
    EQ = Equals(3)
    C = G.add_constraint("109", "Befristung", [[LT, LT], [EQ]])
    print(C)
    bef = G.get_variable("Befristung")
    #bef.set_value(3)

    a = G.get_variable("Blah")
    b = G.get_variable("Blah")

    c = G.get_goal("Ziel")
    d = G.get_goal("Ziel")

    most_relevant_variable = G.get_most_relevant_variable()
    valid_goals = G.get_valid_goals()
    print(most_relevant_variable)
    for valid_goal in valid_goals:
        print(valid_goal)