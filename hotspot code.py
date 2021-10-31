print("HotSPot")
print("HotSpot is a website that has been created to help researchers and physicians to know if the  genetic variations"
      "are reported to be asscoited with cancer")
def account() :
    print(" Create an account")
    name = input("Enter your name:")
    email = input("Enter your e-mail:")
    print("Hello " + name + " a conformation e-mail will be sent to your e-mail " + email)


account()

def gene() :
    print("please  write your gene of interest that you found in breast cancer patient for example: BRCA1 BRCA2 CDH1 EGFR BARD1 RAD51D MSH6 CHEK2 ATM PALB2 MSH6")
    Gene = input("enter the gene name:")
    Variation = input("Enter the the gene variation using the transcript HGVS expressions, e.g. NM_000314.4:c.395G>T:")


gene()

Gene= True
Variation= True
if Gene and Variation:
    print("searching for" + Gene "and"+ Variation)

