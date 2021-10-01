from spacingmodel import *
from app import App


def load_in_facts(m):
    print("hi")


def main():
    m = SpacingModel()
    # fact1 = Fact(
    #     1,
    #     question_type="Family",
    #     question="Gekkonidae, ploceidae, scorpaenidae, siganidae",
    #     answer="Chordata",
    # )
    # m.add_fact(fact1)
    load_in_facts(m)
    app = App("Name", 700, 550)


if __name__ == "__main__":
    main()
