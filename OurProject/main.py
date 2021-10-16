from spacingmodel import *
from app import App
import sys
import os


def load_datasets(file, m, hierarchy):
    f = open(file)
    dict1 = {}
    dict2 = {}
    for line in f:
        split_line = line.strip().split(";")
        if file == "fact.txt":
            fact = Fact(split_line[0], split_line[1], split_line[2], split_line[3])
            if fact.question_type == "Species" and hierarchy:
                m.add_fact(fact)
            elif not hierarchy:
                m.add_fact(fact)
            dict1[fact] = 0
            dict2[split_line[0]] = fact
        else:
            if len(split_line) == 2:
                dict1[split_line[0]] = split_line[1].rstrip().split(",")
    return dict1, dict2


def main(argv):
    m = SpacingModel()
    hierarchy = [False, True][int(argv[1])]
    learned_dict, fact_dict = load_datasets("fact.txt", m, hierarchy)
    tree_dict, throw_away = load_datasets("tree.txt", m, hierarchy)

    app = App(
        "Learning Taxonomic Facts", 700, 550, fact_dict, tree_dict, learned_dict, m
    )
    # save the data from the experiment to a file named results_participant_(specified number).txt
    if not os.path.exists("results"):
        os.makedirs("results")

    if len(argv) == 3:
        data = "results/results_participant_" + str(argv[2]) + ".txt"
    else:
        data = "results/results_participant_unknown.txt"
    m.export_data(data)


if __name__ == "__main__":
    main(sys.argv)
