while True:
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a=7
    b=1
    x=int(input("Enter x: "))

    result=(a*x)-b

    print("E(x) is {}".format(result))

    enc_text=result%26

    print("E(x)%26 is {}".format(enc_text))
    print("The ciphertext is {}".format(letters[enc_text]))




