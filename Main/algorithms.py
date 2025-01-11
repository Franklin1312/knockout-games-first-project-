from random import shuffle, choice
import shelve as s


def sorted(list1: list, reverse: bool = False) -> list:
    """returns the configured list for processing.

    Args:
        list (list): list of participant data
        reverse (bool, optional): reversal of the order. Defaults to False.

    Returns:
        list[str]: configured list
    """
    a=[i for i in list1 if i[3].strip() in ("y",'Y')]
    shuffle(a)
    b=[i for i in list1 if i[3].strip() in("n",'N')]
    shuffle(b)
    experienced_list = a
    inexperienced_list = b
    if reverse:
        return inexperienced_list + experienced_list
    else:
        return experienced_list + inexperienced_list
    


def participants_for_sep(number: int) -> int:
    """returns the number of participants in excess to nearest 2**n which is smaller than the number.

    Args:
        number (int): number of participants

    Returns:
        int: excess number of participants
    """
    counter= 1
    while 2**counter < number:
        counter += 1
    else:
        return 2*(number - 2**(counter - 1))
    


def create_fixtures(dbfile: str) -> tuple:
    """create fixtures for the current round.

    Args:
        number (int): number of paricipants.
        dbfile (str): path to the database file(shelve binary file).

    Returns:
        tuple[list[list[str]], int]: returns a tuple with a list (nested) of the current fixtures and the number of participants who will appear in the next round.
    """
    f = s.open(dbfile)
    no = participants_for_sep(number=len(dict(f)))
    all_list = [[i] + f[i] for i in f]
    fixtures = []
    pool = []
    next_round_number = 0
    if no == 0:
        next_round_number = len(dict(f)) // 2
        pool = all_list.copy()
    else:
        sorted_list = sorted(list1=all_list, reverse=True)
        pool = sorted_list[:no]
    

    while pool != []:
        next_round_number = len(dict(f))- no // 2
        student1 = choice(pool)
        pool.remove(student1)
        student2 = choice(pool)
        pool.remove(student2)
        fixtures.append([student1, student2])
    else:
        return fixtures
