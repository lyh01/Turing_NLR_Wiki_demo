import argparse
import wikipedia as wiki
import requests

#
# Process --input and --question from command line
#

parser = argparse.ArgumentParser(description = "The demo will retrieve a Wikipedia page, and answer a question")
parser.add_argument('-i', '--input', help="input the wiki page, e.g., \"chicago bears\"", type=str, required=True )
parser.add_argument('-q', '--question', help="ask a question, e.g., \"when did the bears move?\"", type=str, required = True)
args = parser.parse_args()

#
# wiki page content in result.content
#
resultWiki = wiki.WikipediaPage(title=args.input)

#
#  set up for API call
#

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'your-api-key-goes-here',

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

print("\nBest answer for \n\nQ: \"{}\"\nA: {}\n\nusing this passage:\n\n\"{}\"\n\n".format(respJSON['question'], respJSON['answers'][0]['Answer'], respJSON['answers'][0]['Passage']))
