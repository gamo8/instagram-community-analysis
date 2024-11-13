# Exploring Instagram’s Top 100 Influencers with Gephi: Social Network Analysis & Community Mapping
This project provides an in-depth analysis and visualization of Instagram's social network structure by leveraging data collected from popular Instagram accounts and their followers. Using network analysis techniques, this project maps relationships, detects communities, and uncovers influential nodes within the Instagram ecosystem. It utilizes Gephi for visualization and Python for data processing, with the potential to integrate machine learning for deeper insights.

This repository is related to this video:

https://www.youtube.com/watch?v=fnXdmS1Hedw

Instructions:
Please, check readme.txt files for instruction on how to use this software:
There are 2 folder manual scrape and auto scraper
Manual Scraper does the same way I showed in the youtube video
Auto Scraper does it automatically, but I recommend to not overuse it, as your account may be blocked by Instagram.

Open the file “instagram-analysis.gephi” on Gephi to open this graph project.

Gephi Set-up:
-	Import nodes and edges as explained in the video

-	Go to Statistics tab and, under Network Overview, run: Average Degree and Network Diameter

-	Under Community Detection, run Modularity and choose resolution 3
 
-	On the Appearance tab click on Nodes, Cor at the top, Partition and Modularity Class and choose a pallet that you like. Click Apply

-	On the Appearance tab click on Nodes, Size on the top, Rankings and choose In-degree. I used from 1 to 20, you can choose as you like
 
-	On the Appearance tab click on Nodes, Labe Size on the top, Rankings and choose In-degree. I used from 1 to 20, you can choose as you like

-	On Layout, choose ForceAtlas 2, tolerance 0.04, check Approximate Repulsion, Approximation 1.2, Scaling 200, check prevent overlap and Edge weight Influence 0.5. Keep the remaining as default
  

 
References:
Largest 100 Instagram accounts
https://socialblade.com/instagram/top/100/followers
Collect, Process, Visualize - Programming Social Graphs (Instagram, Python, Gephi)
 https://www.youtube.com/watch?v=CgHDt_aKyCc
ForceAtlas2, a Continuous Graph Layout Algorithm for Handy Network Visualization Designed for the Gephi Software https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0098679
Getting Started with Network Data Using Gephi
https://www.youtube.com/watch?v=lPivwXdy9XY
No-Code Instagram API Data Scraping with HAR Files
https://www.youtube.com/watch?v=lQnSTeCOjXQ
Network Analysis with Gephi
https://www.youtube.com/watch?v=WpFZmIJTjA8
 Intro2SNA (Gephi for Twitter Network Analysis, Community Detection and Influencer Analysis)
https://www.youtube.com/watch?v=Bx1uArwfoGM
 Análise de dados | Grafo a partir de perfis do Instagram – Gephi
https://www.youtube.com/watch?v=G946j72_Bb0

Analyzed accounts sorted by number of followers
1.	Instagram - The official account of the Instagram platform.
2.	Cristiano Ronaldo - Portuguese footballer, one of the most famous athletes in the world.
3.	Leo Messi - Argentine footballer, widely regarded as one of the greatest players of all time.
4.	Selena Gomez - American singer, actress, and producer.
5.	Kylie Jenner - American media personality, businesswoman, and member of the Kardashian-Jenner family.
6.	Dwayne Johnson (The Rock) - American actor and former professional wrestler.
7.	Ariana Grande - American singer, songwriter, and actress.
8.	Kim Kardashian - American media personality and businesswoman, member of the Kardashian family.
9.	Beyoncé - American singer, songwriter, and actress, one of the best-selling music artists.
10.	Khloé Kardashian - American media personality and businesswoman, member of the Kardashian family.
11.	Nike - Official account of the popular sportswear brand.
12.	Justin Bieber - Canadian singer and songwriter.
13.	Kendall Jenner - American model and media personality, member of the Kardashian-Jenner family.
14.	Taylor Swift - American singer and songwriter known for her storytelling and chart-topping albums.
15.	National Geographic - Media organization focused on nature, science, and history.
16.	Virat Kohli - Indian cricketer and former captain of the Indian national team.
17.	Jennifer Lopez (JLo) - American singer, actress, and dancer.
18.	Nicki Minaj - American rapper, singer, and songwriter.
19.	Neymar Jr - Brazilian footballer, known for his skill and charisma on the field.
20.	Kourtney Kardashian - American media personality and businesswoman, member of the Kardashian family.
21.	Miley Cyrus - American singer, songwriter, and actress.
22.	Katy Perry - American singer and songwriter known for hits like "Roar" and "Firework."
23.	Zendaya - American actress and singer, known for her roles in Euphoria and Spider-Man.
24.	Kevin Hart - American comedian and actor.
25.	Real Madrid C.F. - Spanish football club, one of the most successful in the world.
26.	Cardi B - American rapper and media personality.
27.	LeBron James (King James) - American professional basketball player, considered one of the greatest in NBA history.
28.	Demi Lovato - American singer, songwriter, and actress.
29.	Rihanna - Barbadian singer, actress, and businesswoman.
30.	Chris Brown - American singer, songwriter, and dancer.
31.	Drake (champagnepapi) - Canadian rapper, singer, and actor.
32.	Ellen DeGeneres - American comedian, actress, and former talk show host.
33.	FC Barcelona - Spanish football club with a large global fanbase.
34.	Kylian Mbappé - French footballer known for his speed and skill.
35.	Billie Eilish - American singer-songwriter known for her unique style and hit songs.
36.	UEFA Champions League - Annual European football club competition.
37.	Gal Gadot - Israeli actress known for playing Wonder Woman.
38.	NASA - The United States' space agency.
39.	Shraddha Kapoor - Indian actress and singer in Bollywood films.
40.	Priyanka Chopra - Indian actress and global star, also married to singer Nick Jonas.
41.	Narendra Modi - Prime Minister of India.
42.	Shakira - Colombian singer and songwriter, known for her hits like "Hips Don't Lie."
43.	NBA - National Basketball Association, the premier professional basketball league in the U.S.
44.	Snoop Dogg - American rapper, songwriter, and media personality.
45.	David Beckham - English former footballer and global sports icon.
46.	Dua Lipa - British singer and songwriter.
47.	Alia Bhatt - Indian actress in Bollywood films.
48.	Jennie (BLACKPINK) - South Korean singer and rapper, member of the K-pop group BLACKPINK.
49.	Khaby Lame - Social media personality known for his comedic silent reactions.
50.	Rosé (BLACKPINK) - South Korean singer, member of BLACKPINK.
51.	Katrina Kaif - Indian actress known for her work in Bollywood.
52.	Deepika Padukone - Indian actress, one of Bollywood’s top stars.
53.	Jisoo (BLACKPINK) - South Korean singer and actress, member of BLACKPINK.
54.	Victoria's Secret - American lingerie and beauty retailer.
55.	Neha Kakkar - Indian playback singer.
56.	Gigi Hadid - American model and television personality.
57.	Ronaldinho - Retired Brazilian footballer known for his creativity and skill.
58.	Karim Benzema - French footballer known for his career with Real Madrid.
59.	Premier League - The top-tier English football league.
60.	433 (Football Media) - Popular football (soccer) media account.
61.	BTS - South Korean K-pop group known worldwide.
62.	The Weeknd - Canadian singer, songwriter, and record producer.
63.	Emma Watson - British actress, activist, known for Harry Potter series.
64.	Justin Timberlake - American singer, songwriter, and actor.
65.	Urvashi Rautela - Indian actress and model.
66.	Shawn Mendes - Canadian singer and songwriter.
67.	Jacqueline Fernandez - Sri Lankan actress in Bollywood.
68.	Karol G - Colombian reggaeton singer.
69.	Will Smith - American actor, rapper, and producer.
70.	Salman Khan - Indian film actor and producer in Bollywood.
71.	Anushka Sharma - Indian actress and producer, married to cricketer Virat Kohli.
72.	Marcelo Vieira - Brazilian footballer, known for his career at Real Madrid.
73.	Akshay Kumar - Indian actor known for his work in Bollywood.
74.	V (BTS) - Member of the South Korean boy band BTS.
75.	Marvel Entertainment - Entertainment company known for superhero franchises like the Avengers.
76.	Tom Holland - English actor, known for playing Spider-Man in the Marvel films.
77.	Camila Cabello - Cuban-American singer and songwriter.
78.	Sergio Ramos - Spanish footballer known for his career with Real Madrid.
79.	Anitta - Brazilian singer and songwriter.
80.	Georgina Rodríguez - Model and partner of Cristiano Ronaldo.
81.	Zlatan Ibrahimovic - Swedish footballer known for his unique personality and skill.
82.	Manchester United - English football club with a large global following.
83.	Maluma - Colombian singer and songwriter.
84.	Millie Bobby Brown - English actress, known for Stranger Things.
85.	Paris Saint-Germain (PSG) - French football club known for high-profile players.
86.	Mohamed Salah - Egyptian footballer, plays for Liverpool.
87.	Paul Pogba - French footballer known for his creativity on the field.
88.	ZARA - Popular fashion retail brand.
89.	Bella Hadid - American model.
90.	Disha Patani - Indian actress and model.
91.	Zac Efron - American actor known for High School Musical.
92.	MrBeast - American YouTuber known for his large-scale challenges and philanthropy.
93.	Leonardo DiCaprio - American actor known for films like Titanic and Inception.
94.	Juventus - Italian football club with a strong history.
95.	Chanel - Luxury fashion brand.
96.	Chris Hemsworth - Australian actor known for playing Thor in Marvel films.
97.	Joko Widodo (Jokowi) - President of Indonesia.
98.	Whindersson Nunes - Brazilian comedian and YouTuber.
99.	Travis Scott - American rapper, singer, and record producer.

Possible Niches / Communities identified by chatgpt.com (not what was sorted by Gephi)
1. Social Media Platforms & Media Brands - 8 Accounts
•	Instagram - Platform itself
•	National Geographic - Magazine and media organization
•	NASA - Space agency, educational and scientific media content
•	UEFA Champions League - European football club competition
•	NBA - Professional basketball league
•	Premier League - English football league
•	433 - Football media brand
•	Marvel Entertainment - Entertainment and media brand focused on superhero content
2. Football Clubs & Sports Organizations - 5 Accounts
•	Real Madrid C.F. - Spanish football club
•	FC Barcelona - Spanish football club
•	Manchester United - English football club
•	Paris Saint-Germain (PSG) - French football club
•	Juventus - Italian football club
3. Footballers (Soccer Players) - 13 Accounts
•	Cristiano Ronaldo - Footballer
•	Leo Messi - Footballer
•	Neymar Jr - Footballer
•	Kylian Mbappé - Footballer
•	Virat Kohli - (technically a cricketer, but aligns with athlete category)
•	Karim Benzema - Footballer
•	Sergio Ramos - Footballer
•	Ronaldinho - Retired footballer
•	David Beckham - Retired footballer
•	Zlatan Ibrahimovic - Footballer
•	Mohamed Salah - Footballer
•	Paul Pogba - Footballer
•	Marcelo Vieira - Footballer
4. Musicians & Singers - 26 Accounts
•	Selena Gomez - Singer/Actress
•	Ariana Grande - Singer
•	Beyoncé - Singer
•	Jennifer Lopez (JLo) - Singer/Actress
•	Nicki Minaj - Rapper
•	Miley Cyrus - Singer/Actress
•	Katy Perry - Singer
•	Zendaya - Actress/Singer
•	Demi Lovato - Singer/Actress
•	Rihanna - Singer/Businesswoman
•	Chris Brown - Singer
•	Drake - Rapper
•	Billie Eilish - Singer
•	Shakira - Singer
•	Dua Lipa - Singer
•	Jennie (BLACKPINK) - Singer (K-pop)
•	Rosé (BLACKPINK) - Singer (K-pop)
•	Jisoo (BLACKPINK) - Singer (K-pop)
•	Karol G - Reggaeton Singer
•	The Weeknd - Singer
•	Camila Cabello - Singer
•	Anitta - Singer
•	Maluma - Singer
•	Shawn Mendes - Singer
•	Travis Scott - Rapper
5. Actors and Actresses - 28 Accounts
•	Dwayne Johnson (The Rock) - Actor
•	Kylie Jenner - Media personality and actress
•	Kim Kardashian - Media personality and actress
•	Kourtney Kardashian - Media personality and actress
•	Khloé Kardashian - Media personality and actress
•	Kevin Hart - Comedian/Actor
•	Ellen DeGeneres - Comedian/Actress
•	Gal Gadot - Actress
•	Shraddha Kapoor - Actress
•	Priyanka Chopra - Actress
•	Alia Bhatt - Actress
•	Katrina Kaif - Actress
•	Deepika Padukone - Actress
•	Neha Kakkar - Actress
•	Gigi Hadid - Model/Actress
•	Emma Watson - Actress
•	Urvashi Rautela - Actress/Model
•	Jacqueline Fernandez - Actress
•	Will Smith - Actor
•	Salman Khan - Actor
•	Anushka Sharma - Actress
•	Akshay Kumar - Actor
•	Tom Holland - Actor
•	Millie Bobby Brown - Actress
•	Disha Patani - Actress
•	Zac Efron - Actor
•	Leonardo DiCaprio - Actor
•	Chris Hemsworth - Actor
6. Models & Fashion Icons - 6 Accounts
•	Kendall Jenner - Model
•	Gigi Hadid - Model
•	Bella Hadid - Model
•	Victoria's Secret - Fashion brand, but represents many models
•	Chanel - Fashion brand, represents models/fashion
•	ZARA - Fashion retail brand
7. Politicians & Leaders - 2 Accounts
•	Narendra Modi - Prime Minister of India
•	Joko Widodo (Jokowi) - President of Indonesia
8. Influencers & Content Creators - 3 Accounts
•	Khaby Lame - Social media personality known for silent comedy
•	MrBeast - YouTuber known for large-scale challenges and philanthropy
•	Whindersson Nunes - Brazilian comedian and YouTuber
9. Miscellaneous / Brands - 2 Accounts
•	Nike - Sportswear brand
•	433 - Football content/media brand (also in Sports Media)




