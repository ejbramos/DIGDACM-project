def line_coder(data):
    encoded = list(map(int,str(data))) # Convert string or bits to string then back to int in order to have int data type inside the list
    encoded_signal = [] # Encoded to BAMI-B8Zs signal
    counter = 0 # Counter for the number of bits for the B8Zs scrambling
    lastbit = -1  # initialize as true assuming the first pulse is positive
    numZeros = 0  # Count the number of consecutive zeros at the end of the string
    tempEnc = []
    line_coded_data = ""

    for i in range(len(encoded)):
        if encoded[i] == 0 and i < len(encoded)-1:
            counter += 1
            numZeros += 1
            if counter == 8:
                encoded_signal.extend([0]*3)
                encoded_signal.extend([lastbit, -lastbit, 0, -lastbit, lastbit])
                counter = 0
                numZeros = 0 
        elif encoded[i] == 0 and i == len(encoded)-1:
            encoded_signal.append(0)
        else:
            if numZeros > 0:
                encoded_signal.extend([0]*numZeros)
                numZeros = 0
            counter = 0

            encoded_signal.append(-lastbit)
            lastbit = -lastbit

    for i in range(len(encoded_signal)):
        if encoded_signal[i] == 1:
            tempEnc.append("+") 
        elif encoded_signal[i] == -1:
            tempEnc.append("-")
        else:
            tempEnc.append("0")

    line_coded_data = "".join(tempEnc)           
    return line_coded_data