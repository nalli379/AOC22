with open('day6_input.txt', 'r') as f:
    signal = f.read()

    # i = 0
    # j = 4

    # while True:
    #     marker = signal[i:j]
    #     if len(set(marker)) == 4:
    #         break
    #     else:
    #         i += 1
    #         j += 1

    # print(j)

    i = 0
    j = 14

    while True:
        marker = signal[i:j]
        if len(set(marker)) == 14:
            break
        else:
            i += 1
            j += 1


    print(j)