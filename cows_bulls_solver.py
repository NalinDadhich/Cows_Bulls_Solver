from itertools import combinations
chances = 8
length = 4


def get_all_sols(search_space, guess, cows, bulls):
    new_search_space = set()
    all_bull_pos = combinations(range(length), bulls)

    if cows == 0 and bulls == 0:
        for word in search_space:
            has_common = any(word.find(ch) != -1 for ch in guess)
            if not has_common:
                new_search_space.add(word)

    else:
        for bull_pos in list(all_bull_pos):
            all_cow_pos = combinations(list(set(range(length)) - set(list(
                bull_pos))), cows)
            for cow_pos in list(all_cow_pos):
                # print("bull pos: ", bull_pos, end=" ")
                # print("cow pos: ", cow_pos)
                for word in search_space:
                    bull_result = all(word[p] == guess[p] for p in bull_pos)
                    cow_result = all(word.find(guess[p]) != -1 and word.find(
                        guess[p]) != p and word.find(guess[p]) not in bull_pos for p in cow_pos)
                    if bull_result and cow_result:
                        new_search_space.add(word)

    return new_search_space


if __name__ == "__main__":
    pos = []
    f = open('dictionary.txt')
    all_words = f.readlines()
    rel_words = []
    search_space = set()
    for word in all_words:
        if len(word) == 5:
            rel_words.append(word)

    search_space = set(rel_words)
    while chances:
        guess = input("What did you tell: ")
        cows = input("Cows: ")    #Cows: correct letter, not in exact position
        bulls = input("Bulls: ")  #Bull: correct letter, in exact position
        print("Initial search area: ", len(search_space))
        search_space = get_all_sols(search_space, guess, int(cows), int(bulls))
        for w in search_space:
            print(w[:-1], end=", ")
        print("Final search area: ", len(search_space))
        chances = chances-1

