"""
ukrainian target game
"""
import random
def generate_grid():
    """
    generates letters for game
    >>> 1==1
    True
    """
    alphavit=['а','б','в','г','ґ','д','е','є','ж','з','и','і','ї','й','к','л','м','н'\
        ,'о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ю','я']
    iter_num=0
    grid=[]
    while iter_num<5:
        letter=random.choice(alphavit)
        if letter in grid:
            continue
        iter_num+=1
        grid.append(letter)
    return grid
def generate_part():
    """
    generates part of language
    >>> 1==1
    True
    """
    parts=["noun", "verb", "adjective", "adverb"]
    part=random.choice(parts)
    return part
#print(generate_grid())