from spacingmodel import *
from app import App


def add_fact(m, app, fact1):
    m.add_fact(fact1)


def main():
    app = App("Name", 700, 550)
    m = SpacingModel()
    fact1 = (1, "What Phylum are these families?", "Gekkonidae, ploceidae, scorpaenidae, siganidae", "Chordata")
    add_fact(m, app, fact1)


if __name__ == "__main__":
    main()