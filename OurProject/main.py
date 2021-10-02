from spacingmodel import *
from app import App


def load_datasets(file, m):
    f = open(file)
    dict1 = {}
    for line in f:
        split_line = line.split(";")
        if file == "fact.txt":
            fact = Fact(split_line[0], split_line[1], split_line[2], split_line[3])
            if fact.question_type == "Species":
                m.add_fact(fact)
            dict1[fact] = 0
        else:
            if len(split_line) == 2:
                dict1[split_line[0]] = split_line[1].rstrip().split(",")
    return dict1


def main():
    m = SpacingModel()
    fact_dict = load_datasets("fact.txt", m)
    tree_dict = load_datasets("tree.txt", m)
    app = App("Name", 700, 550, fact_dict, tree_dict, m)


if __name__ == "__main__":
    main()
