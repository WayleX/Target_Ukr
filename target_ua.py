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
def get_words(f_1, letters):
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> 1==1
    True
    """
    words=[]
    with open(f_1,'r', encoding="utf-8") as file:
        for line in file:
            x_list=line.strip().split()
            if len(x_list)<2:
                continue
            x_2_list=x_list[1]
            if len(x_list[0])>5:
                continue
            if not x_list[0][0] in letters:
                continue
            if x_2_list[0:2]=="/n" or x_2_list[0:4]=="noun":
                words.append((x_list[0],"noun"))
            if x_2_list[0:2]=="/v" or x_2_list[0:1]=="v":
                words.append((x_list[0],"verb"))
            if x_2_list[0:4]=="/adj" or x_2_list[0:3]=="adj":
                words.append((x_list[0],"adjective"))
            if x_2_list[0:3]=="adv":
                words.append((x_list[0],"adverb"))
    return words
def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    checks user words in list
    return guessed and not guessed words
    >>> 1==1
    True
    """
    right_words=[]
    for i in user_words:
        if not i[0] in letters:
            continue
        if (i,language_part) in dict_of_words:
            right_words.append(i)
    #print(f"Guessed words:{right_words}")
    not_guessed=[]
    for i in dict_of_words:
        if not i[0] in user_words and language_part==i[1]:
            not_guessed.append(i[0])
    #print(f"Not guessed words:{not_guessed}")
    return right_words,not_guessed