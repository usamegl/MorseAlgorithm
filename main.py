def KodTablosu(char):

    tablo = {

        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",

        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",

        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",

        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",

        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",


        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",

        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",

        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",

        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",

        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",


        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",

        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",


        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",

        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"

    }


    return tablo[char]



def encoding(metin):

    metin, biten_metin = metin.upper(), ""

    for sembol in metin:

        if sembol.isalnum():

            biten_metin += KodTablosu(sembol) + " "


    return biten_metin



def decoding(metin):

    metin, biten_metin = metin.upper(), ""

    for code in metin.split():

        biten_metin += KodTablosu(code)


    return biten_metin



def assembly(mod):

    metin = str(input("[+] Metin Giriniz - "))


    if mod == 0:

        biten_metin = encoding(metin)

    else:

        biten_metin = decoding(metin)


    print("\n »» Şifreleme Sonucu ««")

    print(biten_metin)



def main():

    print("[x] Mors Kriptografi Algoritması. [x]")

    print(" • 0. Encoding modu.\n • 1. Decoding modu.")


    mod = int(input("[?] Program Modu Seçiniz - "))

    assembly(mod)



if __name__ == '__main__':

    main()
    