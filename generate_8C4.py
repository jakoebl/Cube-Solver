lookup = ['00001111', '00010111', '00011011', '00011101', '00011110', '00100111', '00101011', '00101101', '00101110', '00110011', '00110101', '00110110', '00111001', '00111010', '00111100', '01000111', '01001011', '01001101', '01001110', '01010011', '01010101', '01010110', '01011001', '01011010', '01011100', '01100011', '01100101', '01100110', '01101001', '01101010', '01101100', '01110001', '01110010', '01110100', '01111000', '10000111', '10001011', '10001101', '10001110', '10010011', '10010101', '10010110', '10011001', '10011010', '10011100', '10100011', '10100101', '10100110', '10101001', '10101010', '10101100', '10110001', '10110010', '10110100', '10111000', '11000011', '11000101', '11000110', '11001001', '11001010', '11001100', '11010001', '11010010', '11010100', '11011000', '11100001', '11100010', '11100100', '11101000', '11110000', '11110000', '11101000', '11100100', '11100010', '11100001', '11011000', '11010100', '11010010', '11010001', '11001100', '11001010', '11001001', '11000110', '11000101', '11000011', '10111000', '10110100', '10110010', '10110001', '10101100', '10101010', '10101001', '10100110', '10100101', '10100011', '10011100', '10011010', '10011001', '10010110', '10010101', '10010011', '10001110', '10001101', '10001011', '10000111', '01111000', '01110100', '01110010', '01110001', '01101100', '01101010', '01101001', '01100110', '01100101', '01100011', '01011100', '01011010', '01011001', '01010110', '01010101', '01010011', '01001110', '01001101', '01001011', '01000111', '00111100', '00111010', '00111001', '00110110', '00110101', '00110011', '00101110', '00101101', '00101011', '00100111', '00011110', '00011101', '00011011', '00010111', '00001111']


def string_list():
    for i in range(0, 5):
        for j in range(i + 1, 6):
            for k in range(j + 1, 7):
                for l in range(k + 1, 8):
                    result = ""
                    temp = [0, 0, 0, 0, 0, 0, 0, 0]
                    temp[i] = 1
                    temp[j] = 1
                    temp[k] = 1
                    temp[l] = 1
                    for element in temp:
                        result += str(element)
                    lookup.append(result)
    lookup.reverse()
