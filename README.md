
This simple code demonstrates how to perform semantic search using  Microsoft [Turing-NLG's](https://www.microsoft.com/en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft/) question and answer (Q&A) API. You will need to substitute in your own API key.

T-NLG is a transformer-based language model, it has 78 Transformer layers with a hidden size of 4256 and 28 attention heads. Transformer-based language models have improved the state of the art on nearly every downstream natural language processing (NLP) task, including question answering, conversational agents (bots), and document understanding among others.

```
python wiki-demo.py --help
usage: wiki-demo.py [-h] -p PAGE -q QUESTION

This demo will retrieve a Wikipedia page (--page), and answer a question (--question) based on its content

optional arguments:
  -h, --help            show this help message and exit
  -p PAGE, --page PAGE
                        input the wiki page, e.g., "chicago_bears"
  -q QUESTION, --question QUESTION
                        ask a question, e.g., "when did the bears move?"
```
Example:
```
>python ./wiki-demo.py --page 2020_Chicago_Bears_season --question "what trades did the bears make for 2019?"

Best answer for 

Q: "what trades did the bears make for 2019?"
A: wide receivers Reggie Davis, Thomas Ives, and Alex Wesley; tight end Dax Raymond; offensive linemen Dino Boyd and Sam Mustipher; linebacker James Vaughters; and defensive backs Xavier Crawford and Stephen Denmark to reserve/future contracts
   (score: 0.55)

using this passage:

"Shortly after the 2019 season came to an end, the Bears signed wide receivers Reggie Davis, Thomas Ives, and Alex Wesley; tight end Dax Raymond; offensive linemen Dino Boyd and Sam Mustipher; linebacker James Vaughters; and defensive backs Xavier Crawford and Stephen Denmark to reserve/future contracts. All nine players were members of the practice squad in 2019, with Vaughters being the only one to play in the regular season that year. On January 6, tight end Darion Clark was also signed to a reserve/future contract; a former college basketball player, Clark had last played football in high school but participated in the USC Trojans football Pro Day in 2018."

>python ./wiki-demo.py --page national_football_league --question "what happened to the bears in 1932?"

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
