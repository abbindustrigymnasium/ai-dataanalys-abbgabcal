# TetrAI
## Innehåll
  - [Projektbeskrivning](#projektbeskrivning)
  - [Resurser](#resurser)
  - [Krav](#krav)
  - [Filer](#filer)
  - [Potentiella förbättringar](#potentiella-förbättringar)
  - [Svårigheter med projektet](#svårigheter-med-projektet)
  - [Kända fel](#kända-fel)

## Projektbeskrivning
Ett projekt där en AI ska spela en klon av tetris. Planen är att försöka använda sig av deep Q-learning för att lära upp AI:n. Tetrisklonen är en klon av tetris specialgjord för att en AI ska kunna spela. 

## Resurser
- [tf_agents dokumentation](https://www.tensorflow.org/agents)
- [Tensorflow dokumentation](https://www.tensorflow.org/api_docs)
- [Exempel på DQN](https://colab.research.google.com/github/tensorflow/agents/blob/master/docs/tutorials/1_dqn_tutorial.ipynb#scrollTo=KEHR2Ui-lo8O)

## Krav
* Bibliotek
  * Tensorflow
  * tf_agents
  * numpy
  * ImageIo
  * pygame (krävs endast för att använda ditt eget spelande som träningsdata)
  * 
* Hårdvara
  * Cuda kompatibelt grafikkort (testat med gtx 1060)
* Mjukvara
  * Python (testat på 3.8.8)
  * NVIDIA Cuda (testat med cuda 11)
  * ffmpeg (krävs för att skapa videos)

## Filer
### gameInputModel
Tensorflowagent som använder sig utav deep q learning för att lära sig tetris. Börjar med att samla in information när du spelar tetris och lär sig utav det. Använder sig utav miljön TFGameInputEnv för att kommunicera med spelet. Kräver pygame. 
### TFAgent
Tensorflowagent som anvädner sig utav deep q learning gör att lära sig tetris. Kommunicerar med spelet genom TFEnv
### Environment
Vanlig miljö som kan användas utan tensorflow med exempelvis ett vanligt q-table.  
### tetris
En "tetrismotor". En slags "backend" som man kan koppla valfri klient, exempelvis pygame eller en AI till för att spela tetris. 
### game
Vanligt hederligt tetrisspel. Bygger på pygame och kräver pygame installerat för att kunna köras. 

## Potentiella förbättringar
* En AI som kan starta upp sitt lärande utifrån videos på andra som spelar tetris. Exempelvis proffs. Liknande som AlphaGo som började med att titta på stora mängder omgångar av spelet Go. 
* En annan algoritm. Deep q-learning är kraftfullt men kanske inte den lämpligaste metoden för en AI att bli bra på tetris. Någon variant på genetisk algoritm hade förmodligen kunnat fungera bättre med mindre träning. 

## Svårigheter med projektet
* Hela maskininlärningsbiten har varit svår men framförallt att skapa fungerande miljöer och att göra det möjligt att samla in data genom att man spelar spelet. Då det krävdes att man var tvungen att skapa en spelklient som kunde imitera en tf_agents miljö vilket krävde att man gick lite djupare in i tensorflow samt att det inte fanns någon dokmentation på internet som jag kunde hitta gällande just detta. 

## Kända fel
* I game.py visas inte korrekt level på skärmen. 
* Ingen av maskinlärningsagenterna har lärt sig tetris bra. Oklart om det beror på något fel eller endast brist på tid och data. 
