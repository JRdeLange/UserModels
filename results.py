import sys
import os


def open_results(folder):
    for filename in os.listdir(folder):
        name = filename.split("_")[-1][:-4]
        condition = filename.split("_")[1] == "True"
        questions = -1
        facts_encountered = {}
        learned_species = set()
        learned_non_species = set()
        f = open(folder + "/" + filename)
        for line in f.readlines()[1:]:
            split_line = line.split(",")
            trial, response, first, rt, correct, fact_id, q_type = (
                split_line[0],
                split_line[1],
                split_line[2],
                split_line[4],
                int(split_line[5] == "True"),
                split_line[6],
                split_line[7],
            )
            questions += 1
            if fact_id not in facts_encountered:
                facts_encountered[fact_id] = correct
            else:
                facts_encountered[fact_id] = (
                    facts_encountered[fact_id] + correct
                ) * correct
                if facts_encountered[fact_id] == 2:
                    if q_type == "Species":
                        learned_species.add(fact_id)
                    else:
                        learned_non_species.add(fact_id)
        print(
            f"{name}, Condition: {condition}, Questions: {questions}, Unique Questions: {len(facts_encountered)}"
            f", Learned Species: {len(learned_species)}, Learned Non-species: {len(learned_non_species)}"
        )


def main():
    open_results("results")


if __name__ == "__main__":
    main()
