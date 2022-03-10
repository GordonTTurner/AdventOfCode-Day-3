def decToBin(num):
  return "{0:b}".format(int(num))

def binToDec(num):
  return int(num, 2)

# ---- PART II ----

def get_rating(diagnostic_list = [], oxygen = True, idx = 0):
    one_list = []
    zero_list = []

    for line in diagnostic_list:
      one_list.append(line) if int(line[idx]) else zero_list.append(line)

    if oxygen:
      if len(one_list) == len(zero_list) == 1:
        return ''.join(one_list if int(one_list[0][idx]) else zero_list)
      else:
        return get_rating(one_list if len(one_list) >= len(zero_list) else zero_list, 1, idx + 1)
    else:
      if len(one_list) == len(zero_list) == 1:
        return ''.join(one_list if not int(one_list[0][idx]) else zero_list)
      else:
        return get_rating(one_list if len(one_list) < len(zero_list) else zero_list, 0, idx + 1)


# ---- MAIN ----

binary = [str.strip(line) for line in open('/content/drive/MyDrive/Advent/advent3.txt', 'r')]
countZero = [0] * 12
countOne = [0] * 12
γ = ε = 0

# ---- PART I ----

for i in range(12):
  for line in binary:
    # If ith binary = 1, count 1 goes up, else count 0 goes up
    if int(line[i]):
      countOne[i] += 1
    else:
      countZero[i] += 1
  # Add binary digit to γ and ε based on most and
  # least common binary for the ith index
  γ += int(countOne[i] > countZero[i]) * 10 ** (11 - i)
  ε += int(countOne[i] < countZero[i]) * 10 ** (11 - i)
print('\nPART I:\n')
dec_γ = binToDec(str(γ))
print(f'γ: {γ} = {dec_γ}')
dec_ε = binToDec(str(ε))
print(f'ε: {ε} = {dec_ε}')
dec_εγ = dec_ε * dec_γ
print(f'εγ: {decToBin(dec_εγ)} = {dec_εγ}')

# ---- PART II ----

print('\nPART II:\n')
O = get_rating(binary, True)
print(f'O: {O} = {binToDec(str(O))}')
CO2 = get_rating(binary, False)
print(f'CO2: {CO2} = {binToDec(str(CO2))}')
life = binToDec(str(O)) * binToDec(str(CO2))
print(f'LSR: {decToBin(life)} = {life}')
