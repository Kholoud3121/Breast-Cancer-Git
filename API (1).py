

import requests

print("HotSPot")
print("HotSpot is a website that has been created to help researchers and physicians to know if the  genetic variations"
      "are reported to be associated with cancer")


def account():
    print("Create an account")
    name = input("Enter your name:")
    email = input("Enter your e-mail:")
    print("Hello " + name +
          " a conformation e-mail will be sent to your e-mail " + email)


def variation():
    return input("Enter the the gene variation using the transcript HGVS expressions, e.g. NM_000314.4:c.395G>T:")


def search(Variation):
    url = "https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts/"
    response = requests.get(url+Variation)
    js = response.json()

    print("The gene is a "+js['transcripts'][0]['description'])


account()
Variation = variation()
print("Searching for" + Variation)
search(Variation)

def Gene():
    return input("Enter the the gene NCBI Gene ID:")


def search(Gene):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id="
    response = requests.get(url+Gene)
    js = response.json()

    print("The gene information is a "+js['Summary'][0]['OtherAliases'])


Gene = Gene()
print("Searching for" + Gene)
search(Gene)
