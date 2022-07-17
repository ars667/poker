curr_prob = 1 / 45

def comb_probs(cards):
    comb = 10 ** 6
    hi_card = 0

    noms = []
    A = [[] for _ in range(4)]
    for i in cards:
        i = str(i)
        x, y = map(int, i.split('$'))
        A[x].append(y)
        noms.append(y)
    for i in range(0, 4):
        A[i].sort()

    k = 0

    for i in range(0, 4):
        if len(A[i]) >= 5:
            hi_m = i
            k += 1
            for j in range(len(A[i])):
                if A[i][j] == A[i][j - 1] + 1:
                    k += 1
    if k >= 5:
        comb = 2
        hi_card = str(max(A[hi_m]))
        our_probs[comb] = 1
    k = 0
    k2 = 0

    for i in range(0, 4):
        if len(A[i]) >= 4:
            hi_m = i
            k += 1
            for j in range(len(A[i])):
                if A[i][j] == A[i][j - 1] + 1:
                    k += 1
                if A[i][j] == A[i][j - 1] + 2:
                    k2 += 1
    if k >= 3 and k2 == 1:
        comb = 2
        hi_card = str(max(A[hi_m]))
        our_probs[comb] = max(curr_prob * 2, our_probs[comb])
    k = 0
    k2 = 0

    for i in range(0, 4):
        if len(A[i]) >= 3:
            hi_m = i
            k += 1
            for j in range(len(A[i])):
                if A[i][j] == A[i][j - 1] + 1:
                    k += 1
                if A[i][j] == A[i][j - 1] + 2:
                    k2 += 1
    if k >= 2 and k2 == 2:
        comb = 2
        hi_card = str(max(A[hi_m]))
        our_probs[comb] = max(curr_prob ** 2, our_probs[comb])
    k = 0
    k2 = 0

    A = [[] for _ in range(13)]
    for i in cards:
        i = str(i)
        x, y = map(int, i.split('$'))
        A[y].append(x)
    for i in range(0, 4):
        A[i].sort()

    for i in range(0, 13):
        if len(A[i]) >= 3:
            hi_m = i
            k = 1
            for j in range(len(A[i])):
                if A[i][j] == A[i][j - 1] + 1:
                    k += 1
    if k == 4:
        comb = 3
    if k == 3:
        comb = 7
        if comb == 3:
            hi_card = hi_m
            our_probs[comb] = 1
    k = 0

    for i in range(0, 13):
        if len(A[i]) >= 3:
            hi_m = i
            k = 1
            for j in range(len(A[i])):
                if A[i][j] == A[i][j - 1] + 1:
                    k += 1
    if k == 4:
        comb = 3
    if k == 3:
        comb = 7
        if comb == 3:
            hi_card = hi_m
            our_probs[comb] = 1
    k = 0

    for i in range(0, 13):
        if len(A[i]) == 2:
            our_probs[3] = max(curr_prob ** 2, our_probs[3])
        if len(A[i]) == 3:
            our_probs[3] = max(curr_prob * 2, our_probs[3])

    for i in range(0, 13):
        if len(A[i]) >= 3:
            hi_card = i
            for j in range(0, 13):
                if (i != j) and (len(A[j]) >= 2):
                    comb = 4
                    our_probs[comb] = 1
    for i in range(0, 13):
        if len(A[i]) >= 2:
            hi_card = i
            for j in range(0, 13):
                if (i != j) and (len(A[j]) >= 2):
                    comb = 4
                    our_probs[comb] = max(curr_prob * 4, our_probs[comb])
    for i in range(0, 13):
        if len(A[i]) >= 2:
            hi_card = i
            for j in range(0, 13):
                if (i != j) and (len(A[j]) >= 1):
                    comb = 4
                    our_probs[comb] = max(curr_prob ** 2 * 6, our_probs[comb])
    k = 0

    A = [[] for _ in range(4)]
    for i in cards:
        i = str(i)
        x, y = map(int, i.split('$'))
        A[x].append(y)
    for i in range(0, 4):
        A[i].sort()

    for i in range(0, 4):
        if len(A[i]) >= 5:
            comb = 5
            hi_card = max(A[i])
            our_probs[comb] = 1

    for i in range(0, 4):
        if len(A[i]) >= 4:
            comb = 5
            hi_card = max(A[i])
            our_probs[comb] = max(curr_prob * 18, our_probs[comb])

    for i in range(0, 4):
        if len(A[i]) >= 3:
            comb = 5
            hi_card = max(A[i])
            our_probs[comb] = max(curr_prob ** 2 * 9, our_probs[comb])

    k = 1

    noms.sort()
    for i in range(1, len(noms)):
        if noms[i] == noms[i - 1] + 1:
            k += 1
            hi_card = i
    if k >= 5:
        comb = 6
        our_probs[comb] = 1
    k = 1

    for i in range(1, len(noms)):
        if noms[i] == noms[i - 1] + 1:
            k += 1
        if noms[i] == noms[i - 1] + 2:
            k2 += 1
            hi_card = i
    if k >= 4 and k2 == 1:
        comb = 6
        our_probs[comb] = max(curr_prob * 6, our_probs[comb])
    k = 1
    k2 = 0

    for i in range(1, len(noms)):
        if noms[i] == noms[i - 1] + 1:
            k += 1
        if noms[i] == noms[i - 1] + 2:
            k2 += 1
            hi_card = i
    if k >= 3 and k2 == 2:
        comb = 6
        our_probs[comb] = max(curr_prob ** 2 * 3, our_probs[comb])

    for i in range(1, len(noms)):
        if noms[i] == noms[i - 1]:
            k += 1
            if k == 2:
                comb = 8
                hi_card = noms[i]
                our_probs[comb] = 1
    k = 0
    for i in range(1, len(noms)):
        if noms[i] == noms[i - 1]:
            k += 1
            if k == 1:
                comb = 9
                hi_card = noms[i]
                our_probs[comb] = 1

    our_probs[8] = max(our_probs[8], 0.1)
    our_probs[9] = max(our_probs[9], 0.33)

    return our_probs

def combination(cards):
    comb = 10 ** 6
    hi_card = 0

    noms = []
    A = [[] for _ in range(4)]
    for i in cards:
        i = str(i)
        x, y = map(int, i.split('$'))
        A[x].append(y)
        noms.append(y)
    for i in range(0, 4):
        A[i].sort()

    k = 0

    for i in range(0, 4):
        if len(A[i]) >= 5:
            hi_m = i
            k += 1
            for j in range(len(A[i])):
                if A[i][j] == A[i][j - 1] + 1:
                    k += 1
    if k >= 5:
        comb = 2
        hi_card = str(max(A[hi_m]))
        return comb, hi_card
    k = 0

    A = [[] for _ in range(13)]
    for i in cards:
        i = str(i)
        x, y = map(int, i.split('$'))
        A[y].append(x)
    for i in range(0, 4):
        A[i].sort()

    for i in range(0, 13):
        if len(A[i]) >= 3:
            hi_m = i
            k = 1
            for j in range(len(A[i])):
                if A[i][j] == A[i][j - 1] + 1:
                    k += 1
    if k == 4:
        comb = 3
    if k == 3:
        comb = 7
        if comb == 3:
            hi_card = hi_m
            return comb, hi_card
    k = 0

    for i in range(0, 13):
        if len(A[i]) >= 3:
            hi_card = i
            for j in range(0, 13):
                if (i != j) and (len(A[j]) >= 2):
                    comb = 4
                    return comb, hi_card
    k = 0

    A = [[] for _ in range(4)]
    for i in cards:
        i = str(i)
        x, y = map(int, i.split('$'))
        A[x].append(y)
    for i in range(0, 4):
        A[i].sort()

    for i in range(0, 4):
        if len(A[i]) >= 5:
            comb = 5
            hi_card = max(A[i])
            return comb, hi_card
    k = 1

    noms.sort()
    for i in range(1, len(noms)):
        if noms[i] == noms[i - 1] + 1:
            k += 1
            hi_card = i
    if k >= 5:
        comb = 6
        return comb, hi_card
    k = 0

    if comb == 7:
        return comb, hi_card

    for i in range(1, len(noms)):
        if noms[i] == noms[i - 1]:
            k += 1
            if k == 2:
                comb = 8
                hi_card = noms[i]
                return comb, hi_card
    k = 0
    for i in range(1, len(noms)):
        if noms[i] == noms[i - 1]:
            k += 1
            if k == 1:
                comb = 9
                hi_card = noms[i]
                return comb, hi_card

    comb = 10
    hi_card = max(noms)
    return comb, hi_card

N = 5

bet = 100

up = 10

hand = ['0$4', '0$6']
table = ['0$1', '0$3', '0$2', '0$5']

if len(table) == 5:
    cards = []
    for card in table:
        cards.append(card)
    for card in hand:
        cards.append(card)

    print(cards)

    print(combination(cards))

    our_comb, our_hi = combination(cards)

    all_cards = []

    for a in range(0, 4):
        for b in range(0, 13):
            card = str(a) + '$' + str(b)
            all_cards.append(card)

    for card in cards:
        all_cards.remove(card)

    ALL = 0
    nice = 0

    print(table, 'AA')
    for i in range(len(all_cards) - 1):
        for j in range(i + 1, len(all_cards)):
            opp_hand = []
            opp_hand.append(all_cards[i])
            opp_hand.append(all_cards[j])
            for card in table:
                opp_hand.append(card)
            # print(opp_hand)
            ALL += 1
            opp_comb, opp_hi = combination(opp_hand)
            if our_comb < opp_comb:
                nice += 1
            if our_comb == opp_comb:
                if our_hi > opp_hi:
                    nice += 1

    prob_of_win = nice / ALL
    prob_of_abs_win = prob_of_win ** N
    if prob_of_abs_win * (bet + up) > bet:
        print('повышать')
    else:
        print('сбрасывать')


    print(nice / ALL)

if len(table) == 4:
    all_cards = []
    ALL = 0
    nice = 0
    for a in range(0, 4):
        for b in range(0, 13):
            card = str(a) + '$' + str(b)
            all_cards.append(card)
    for card in table:
        all_cards.remove(card)
    for card in hand:
        all_cards.remove(card)

    for card_on_table in all_cards:
        table.append(card_on_table)
        cards = []
        for card in table:
            cards.append(card)
        for card in hand:
            cards.append(card)

        print(cards)
        our_comb, our_hi = combination(cards)

        for i in range(len(all_cards) - 1):
            for j in range(i + 1, len(all_cards)):
                opp_hand = []
                opp_hand.append(all_cards[i])
                opp_hand.append(all_cards[j])
                for card in table:
                    opp_hand.append(card)
                # print(opp_hand)
                ALL += 1
                opp_comb, opp_hi = combination(opp_hand)
                if our_comb < opp_comb:
                    nice += 1
                if our_comb == opp_comb:
                    if our_hi > opp_hi:
                        nice += 1
        table.remove(card_on_table)
    print(nice / ALL)

    prob_of_win = nice / ALL
    prob_of_abs_win = prob_of_win ** N
    if prob_of_abs_win * (bet + up) > bet:
        print('повышать')
    else:
        print('сбрасывать')

if len(table) == 3:
    our_probs = [0]*12
    opp_probs = [0]*12
    cards = []
    for card in table:
        cards.append(card)
    for card in hand:
        cards.append(card)

    our_probs = comb_probs(cards)
    print(our_probs)
    all_cards = []
    for a in range(0, 4):
        for b in range(0, 13):
            card = str(a) + '$' + str(b)
            all_cards.append(card)
    for card in table:
        all_cards.remove(card)
    for card in hand:
        all_cards.remove(card)
    print(all_cards)

    for i in range(0, len(all_cards)-1):
        for j in range(i, len(all_cards)):
            opp_probs_local = [0]*12
            opp_hand = []
            opp_hand.append(all_cards[i])
            opp_hand.append(all_cards[j])
            for card in table:
                opp_hand.append(card)
            opp_probs_local = comb_probs(cards)
            chance_of_win = 0
    for i in range(0, 12):
        opp_probs[i] += opp_probs_local[i]
    for i in range(0, 12):
        opp_probs[i] =  opp_probs[i] / 47
    print(opp_probs)
    for i in range(0, 12):
        sum_probs = 0
        for j in range(0, i):
            sum_probs += our_probs[j]
        chance_of_win += sum_probs * opp_probs[i]
    if chance_of_win ** N * (bet + up) > bet:
        print('повышать')
    else:
        print('сбрасывать')

