import copy

grid = ["EECA",
        "ALEP",
        "HNBO",
        "QTTY"]

word_dict = {}

words_found = []


def construct_word(letter_cords):
    word = ''
    dict_branch = word_dict

    for cord in letter_cords:
        x = cord[0]
        y = cord[1]
        letter = grid[y][x]
        word += letter
        if letter in dict_branch:
            dict_branch = dict_branch[letter]
        else:
            return word, 'fail'
    if 'is_a_word_hack' in dict_branch:
        # found a full word
        return word, "full_match"
    else:
        return word, "partial_match"


def search(current_cord, previous_cords):
    x = current_cord[0]
    y = current_cord[1]
    new_cords = copy.deepcopy(previous_cords)
    new_cords.append(current_cord)
    word, match_type = construct_word(new_cords)
    print(word)
    if match_type == 'full_match':
        global words_found
        if word not in words_found:
            words_found.append(word)
        print("found " + word)
    elif match_type == 'fail':
        # prune branches if no word starts with what we got so far
        print("fail on " + word)
        return
    for next_y in range(max(y-1,0), min(y+2, len(grid))):
        for next_x in range(max(x-1,0), min(x+2, len(grid[0]))):
            next_cord = (next_x, next_y)
            if next_cord not in new_cords:
                search(next_cord, new_cords)


def build_dict():
    with open("words.txt") as f:
        for word in f:
            word = word.strip()
            dict_branch = word_dict
            for letter in word:
                letter = letter.upper()
                if letter not in dict_branch:
                    dict_branch[letter] = {}
                dict_branch = dict_branch[letter]
            dict_branch['is_a_word_hack'] = {}
    print('dict done')

build_dict()
for y in range(len(grid)):
    for x in range(len(grid[0])):
        print("searching " + str(x) + " " + str(y))
        search((x,y), [])

print(words_found)
print(len(words_found))
