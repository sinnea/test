from unicodedata import name
import requests

mail = "sinneadoe@gmail.com"
pass_mail = "mypasswordisgreat12!"

def parse_response(response):
    emails = response.get("emails")
    return emails

def main():
    r = requests.get('https://gmail.com/api', auth=(mail, pass_mail))
    response = r.json()
    print(parse_response(response))

if __name__ == "__main__":
    main()
