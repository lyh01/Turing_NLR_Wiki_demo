
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
   (score: 0.95)
   
using this passage:

"On June 24, 1922, the APFA changed its name to the National Football League (NFL).In 1932, the season ended with the Chicago Bears (6–1–6) and the Portsmouth Spartans (6–1–4) tied for first in the league standings. At the time, teams were ranked on a single table and the team with the highest winning percentage (not including ties, which were not counted towards the standings) at the end of the season was declared the champion; the only tiebreaker was that in the event of a tie if two teams played twice in a season, the result of the second game determined the title (the source of the 1921 controversy). This method had been used since the league's creation in 1920, but no situation had been encountered where two teams were tied for first."
```

Output example:

```

{'answers': [{'Answer': 'the season ended with the Chicago Bears (6–1–6) and '
                        'the Portsmouth Spartans (6–1–4) tied for first in the '
                        'league standings',
              'EndTextOffset': 866,
              'Highlights': [{'SpanEnd': 129,
                              'SpanScore': 0.5271576,
                              'SpanStart': 125,
                              'Text': 'Bears'}],
              'Passage': 'On June 24, 1922, the APFA changed its name to the '
                         'National Football League (NFL).In 1932, the season '
                         'ended with the Chicago Bears (6–1–6) and the '
                         'Portsmouth Spartans (6–1–4) tied for first in the '
                         'league standings. At the time, teams were ranked on '
                         'a single table and the team with the highest winning '
                         'percentage (not including ties, which were not '
                         'counted towards the standings) at the end of the '
                         'season was declared the champion; the only '
                         'tiebreaker was that in the event of a tie if two '
                         'teams played twice in a season, the result of the '
                         'second game determined the title (the source of the '
                         '1921 controversy). This method had been used since '
                         "the league's creation in 1920, but no situation had "
                         'been encountered where two teams were tied for '
                         'first.',
              'PassageStart': 11,
              'Score': 0.9485014524000001,
              'SpanEnd': 212,
              'SpanStart': 91,
              'StartTextOffset': 119},
             {'Answer': 'The champions of the NFC receive the George Halas '
                        'Trophy',
              'EndTextOffset': 2704,
              'Highlights': [{'SpanEnd': 82,
                              'SpanScore': 0.8569981,
                              'SpanStart': 78,
                              'Text': 'Bears'}],
              'Passage': 'The champions of the NFC receive the George Halas '
                         'Trophy, named after Chicago Bears founder George '
                         'Halas, who is also considered as one of the '
                         'co-founders of the NFL. The AFC champions receive '
                         'the Lamar Hunt Trophy, named after Lamar Hunt, the '
                         'founder of the Kansas City Chiefs and the principal '
                         'founder of the American Football League. Players on '
                         'the winning team also receive a conference '
                         'championship ring.',
              'PassageStart': 60,
              'Score': 0.028954686,
              'SpanEnd': 55,
              'SpanStart': 0,
              'StartTextOffset': 2296},
             {'Answer': 'the Minnesota Vikings failed to make their selection '
                        'on time. The Jacksonville Jaguars and Carolina '
                        'Panthers were able to make their picks before the '
                        'Vikings were able to use theirs',
              'EndTextOffset': 882,
              'Highlights': [],
              'Passage': 'This happened in the 2003 draft, when the Minnesota '
                         'Vikings failed to make their selection on time. The '
                         'Jacksonville Jaguars and Carolina Panthers were able '
                         'to make their picks before the Vikings were able to '
                         'use theirs. Selected players are only allowed to '
                         'negotiate contracts with the team that picked them, '
                         'but if they choose not to sign they become eligible '
                         "for the next year's draft.",
              'PassageStart': 79,
              'Score': 0.009700818808,
              'SpanEnd': 218,
              'SpanStart': 38,
              'StartTextOffset': 495}],
 'question': 'what happened to the bears in 1932?',
 'status': 0}
```
