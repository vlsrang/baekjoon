def max_chicken(number_list):
    #마지막 박스는 안 먹는 경우
    dp1 = [0] * len(number_list)
    dp1[0] = number_list[0]
    dp1[1] = max(number_list[0], number_list[1])

    for i in range(2, len(number_list)-1):
        dp1[i] = max(dp1[i-1], number_list[i]+dp1[i-2])

    #마지막 박스를 먹는 경우
    dp2 = [0] * len(number_list)
    dp2[0] = 0
    dp2[1] = number_list[1]

    for i in range(2, len(number_list)): 
        dp2[i] = max(dp2[i-1], number_list[i]+dp2[i-2])

    result= max(max(dp1), max(dp2)) 

    return result


def main():

  chicken_number = [2,3,4,1]

  print('먹을수 있는 닭다리 최대 개수: ', max_chicken(chicken_number))

if __name__ == "__main__":
    main()
