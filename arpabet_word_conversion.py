import json
import cv2 as cv

# substitute pairings are "ARPAbet notation" : "set of letters that can sound like this"
vowel_substitutes =  { "AA":"alo",
                        "AE":"a",
                        "AH":"ui",
                        "AO":"o",
                        "AW":"ou",
                        "AX":"a",
                        "AXR":"er",
                        "AY":"Iy",
                        "EH":"ea",
                        "ER":"ir",
                        "EY":"A", # changed ai to A
                        "IH":"ie",
                        "IX":"ei",
                        "IY":"E", # changed ea to E
                        "OW":"O", # changed oa to O
                        "OY":"oy",
                        "UH":"ou",
                        "UW":"ou",
                        "UX":"u"}
consonant_substitutes = {   "B":"b",
                            "CH":"ch",
                            "D":"d",
                            "DH":"th",
                            "DX":"tt",
                            "EL":"le",
                            "EM":"M", # changed m to M
                            "EN":"N", # changed on to N
                            "F":"f",
                            "G":"g",
                            "HH":"h",
                            "H":"h",
                            "JH":"j",
                            "K":"kqc",
                            "L":"l",
                            "M":"m",
                            "N":"n",
                            "NG":"ng",
                            "NX":"nn",
                            "P":"p",
                            "Q":"-",
                            "R":"r",
                            "S":"cs", # c or s can make this sound
                            "SH":"sh",
                            "T":"t",
                            "TH":"th",
                            "V":"v",
                            "W":"wui",
                            "WH":"wh", # should be h-Superscript
                            "Y":"y",
                            "Z":"z",
                            "ZH":"s"}

# uppercase_combos = { "IY"
#
#
# }
def main():
    with open("arpabetTable.json", "r") as json_file:
        arpabet_table = json.load(json_file)

        key = input("what word would you like to convert? ")
        key = key.strip("\n").upper() if key != '' else 0
        val = arpabet_table[key] if key in arpabet_table.keys() else 0

        if not key or not val:
            print("word does not exist in dictionary")
            main()

        key_as_list = list(key.lower())
        val_as_list = val.split()

        key_pointer = 0
        val_pointer = 0
        print("x_as_list: ", x_as_list)
        print("val_as_list: ", val_as_list, "\n")
        main()

if __name__ == "__main__":
    main()
