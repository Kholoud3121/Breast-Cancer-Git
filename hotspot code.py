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
    print("please choose write your gen of interest that you found in breast cancer patient for example: BRCA1 BRCA2 CDH1 EGFR BARD1 RAD51D MSH6 CHEK2 ATM PALB2 MSH6")
    Gene = input("enter the gene name:")
    Variation = input("Enter the the gene variation using the transcript code 'NM'")


gene()

Gene= True
Variation= True
# if Gene and Variation:
#     print("Searching for" + Gene "and"+ Variation)