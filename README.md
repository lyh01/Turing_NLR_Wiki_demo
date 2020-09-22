
This simple code demonstrates how to perform semantic search using  Microsoft's [Turing-NLG](https://www.microsoft.com/en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft/), a 17-billion-paramater language model question and answer (Q&A) API. You will need to substitute in your own API key.
```
python wiki-demo.py --help
usage: wiki-demo.py [-h] -i INPUT -q QUESTION

The demo will retrieve a Wikipedia page, and answer a question

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input the wiki page, e.g., "chicago bears"
  -q QUESTION, --question QUESTION
                        ask a question, e.g., "when did the bears move?"
```
Example:
```
python ./wiki-demo.py --input national_football_league --question "what happened to the bears in 1932?"

question: what happened to the bears in 1932?

Best answer for 

Q: "what happened to the bears in 1932?"
A: the season ended with the Chicago Bears (6–1–6) and the Portsmouth Spartans (6–1–4) tied for first in the league standings

using this passage:

"On June 24, 1922, the APFA changed its name to the National Football League (NFL).In 1932, the season ended with the Chicago Bears (6–1–6) and the Portsmouth Spartans (6–1–4) tied for first in the league standings. At the time, teams were ranked on a single table and the team with the highest winning percentage (not including ties, which were not counted towards the standings) at the end of the season was declared the champion; the only tiebreaker was that in the event of a tie if two teams played twice in a season, the result of the second game determined the title (the source of the 1921 controversy). This method had been used since the league's creation in 1920, but no situation had been encountered where two teams were tied for first."
```
