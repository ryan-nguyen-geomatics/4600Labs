#assigning upper letters and lowercase letters an integer to be converted to ROT13
upperletter = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
         'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
         'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

uppernumber = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
         11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
         21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y'}

lowerletter = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
         'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
         'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

lowernumber = {0: 'z', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
         11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
         21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y'}

# ROT13 ENCODER AND DECODER

message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
list = [] #array used to store values
for i in message:
    if i.isalpha(): # to parse message if its upper letter
        if i.isupper():
            let2num = (upperletter[i]+13)%26 # shifting by 13 and taking the remainder to correspond with the shift
            list += uppernumber[let2num] # the result of the shift stored in array

        elif i.islower(): # to parse message if its lower letter
            let2num = (lowerletter[i]+13)%26
            list += lowernumber[let2num]
    else: # to parse for non alphabet and leave as is
        list += i

print('Message Decoded: ', ''.join(list)) # joins the array together to make a sentence

# Encoding the decoded message
message2 = "Caesar cipher? I much prefer Caesar salad!"

list2 = []
for i in message2:
    if i.isalpha():
        if i.isupper():
            let2num = (upperletter[i]+13)%26
            list2 += uppernumber[let2num]

        elif i.islower():
            let2num = (lowerletter[i]+13)%26
            list2 += lowernumber[let2num]
    else:
        list2 += i

print('Message Encoded: ', ''.join(list2))


# BONUS INPUT
ask = input("Give me a message to encode! ")

list3 = []
for i in ask:
    if i.isalpha():
        if i.isupper():
            let2num = (upperletter[i]+13)%26
            list3 += uppernumber[let2num]

        elif i.islower():
            let2num = (lowerletter[i]+13)%26
            list3 += lowernumber[let2num]
    else:
        list3 += i

print(''.join(list3))

ask2 = input("Give me a message to decode! ")

list4 = []
for i in ask2:
    if i.isalpha():
        if i.isupper():
            let2num = (upperletter[i]+13)%26
            list4 += uppernumber[let2num]

        elif i.islower():
            let2num = (lowerletter[i]+13)%26
            list4 += lowernumber[let2num]
    else:
        list4 += i

print(''.join(list4))


