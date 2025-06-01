def raise_to_power(base_num, power_num):
    cur = 1
    for num in range(power_num):
        cur = cur *base_num
    return cur
print(raise_to_power(2,7), pow(2,7))