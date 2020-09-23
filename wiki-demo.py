import argparse
import wikipedia as wiki
import requests

#
# Process --page and --question from command line
#

parser = argparse.ArgumentParser(description = "This demo will retrieve a Wikipedia page (--page), and answer a question (--question) based on the page content")
parser.add_argument('-p', '--page', help="input the wiki page, e.g., \"chicago_bears\"", type=str, required=True )
parser.add_argument('-q', '--question', help="ask a question, e.g., \"when did the bears move?\"", type=str, required = True)
args = parser.parse_args()

try:
    resultWiki = wiki.WikipediaPage(title=args.page)
except:
    print("\nAn error occurred while retrieving from Wikipedia. Please ensure the wiki page does exist\n")
    exit(12)

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '130743a0539e4c82962b1c2567a57e54',
}

params = {

}

body = {
    "Query": "",
    "Document": [  ]
 }

body['Document'] = resultWiki.content.split("\n")
body['Query'] = args.question

try:

    resultREST = requests.post("https://turing.azure-api.net/answer/v1/", headers = headers, params = params, json=body)
    respJSON = resultREST.json()

except Exception as e:
    print("Error: {}".format(e))

print("\nBest answer for \n\nQ: \"{}\"\nA: {}\n   (score: {:.2f})\n\nusing this passage:\n\n\"{}\"\n\n".
      format(respJSON['question'], respJSON['answers'][0]['Answer'], respJSON['answers'][0]['Score'],
      respJSON['answers'][0]['Passage'], 
      ))
