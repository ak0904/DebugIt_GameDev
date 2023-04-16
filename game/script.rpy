define n = Character("Raaha")
define e = Character("Entity")
define l = Character("Love")
define i = Character("Isa")
define g = Character("Grandma")
define config.default_fullscreen = True 
label start:
scene bg str
"TW : Mentions of murder, death, violence and self-harm."
"For best experience, use headphones and maximum volume."
scene bg room1
play music "softrain.mp3"
n "My grandma always used to say. Never keep the windows open all the night. Otherwise it opens the portal for the unknown and forbidden."
n "It was a common folkore of her village."
n "I really never believed it as it made no sense to me"
play music "amb.mp3"
n "Years later, I was sitting in my master room which comprised both my bedroom and study room. I was sitting on the bed, staring out through the window."
n "..."
n "I contemplated how unstable had my graph of life had been."
n "In order to gain everything, I ended up losing everything. Money, love and..."
n "Family."
n "Soon, this luxurious bungalow of mine was going to be mortgaged. I was going through a financial crunch."
n "My love had deserted me earlier."
n "Maybe I was the one to walk out of the relationship but his indifference was more than a proof he never wanted me in his life."
n "I put my own self before him. The same thing I had done with my family."
n "I had left them quite long back. Because I wanted the former two things first."
n "There were moments of success and praises but now it seemed, everything was lost. I felt wasted and useless."
n "I had lost everything. And the worst part was, the blame was on me."
n "Guilt had already soaked my soul but now it was of no use. There was point of no return in my life."
n "Each day passing felt like a burden adding to my already broken ship. I was way down with repetance."
n "No hope left. No energy left."
n "\"I had the shiniest wheels, now they're rusting.\""
n "I had heard this line somewhere"
n "..."
n "I wish I could get everything back."
scene bg room1
with fade
scene bg open
play music "softrain.mp3"
n "The wind blew through the window, blowing my hair on face. The moon was shining brightly, decorating the star studded sky. Soft rain added to the night."
play music ["softrain.mp3","wind3.wav"] fadeout 1.0 fadein 1.0
n "I started crying and muffled my voice beneath my pillow. Even though there was no one to hear my weeping, yet I didn't want to make noise."
n "Suddenly, a cold wind blew through the window, leaving a chill in my spine. I remembered my grandma's words."
play music [ "wind3.wav", "amb.mp3" ] fadeout 1.0 fadein 1.0
n "Never keep the windows open all night. Otherwise it opens the portal for the unknown and forbidden."
play music "amb.mp3"
n "I thought for a minute. Was it really true? Even though I never believed in such stuff, today I felt an urge to know the truth."
n "What would really happen if I leave the window open?"
n "I looked towards the window. It was open and I could see the moon, the rain and the invisible wind making the nearby trees sway."
n "What if there was really a portal? A gateway to the unknown. Life had given me loads of trouble. This gamble wouldn't have make much of a difference to. Just a night, with open windows."

menu:
        "What you made me choose?"

        "And I decided to do the forbidden.":

         jump forbidden

        "On other hand, I didn't really feel like disobeying my grandma's words.":

         jump one_a

label forbidden:
scene bg room2
with fade
play music "softrain.mp3"
n "I had taken a lot of risks in my life. Many discrete choices led me to several paths of my life."
n "How could it really affect me if a mere window is left open for the entire night."
n "I was too melancholic and tired to debate in my mind on this topic."
n "Let it be open. Let's see what gateway is hiding behind that window."
n "My energy went into crying, thinking about my present situation, the real issue of my life."
n "I kept my face buried inside the pillow, acid rain leaking from my eyes."
n "Soon, the midnight rain lulled me to sleep."
scene bg window2
with fade
stop music
"..."
"...."
"....."
play music "thunder.mp3"
scene bg open
with fade
n "A sudden thunder awoke me from the dead sleep. I had heard many thunders in my life but this one felt like the lightning struck right through my heart."
scene bg moon2
with fade
play music "thunder.mp3"
n "I lifted my face from the pillow and faced the window. Rubbing my teary eyes, it was a blurred scenery for me."
n "It was raining heavily. And there were flashes of lightning bolts now and then."
play music "thunder.mp3"
scene bg moon
with hpunch
n "The thunder continued happening and with each strike, it felt that my entire room was shaking."
n "I rubbed my eyes carelessly and tried to focus on the window."
scene bg bigmoon
with dissolve
n "Strangely, the moon looked very big enough."
scene bg tree
play music "wtree.mp3"
n "The trees were swaying like crazy."
n "I don't know why I was feeling so terrible."
stop music
n "When out of a sudden, everything came to a standstill."
n "The trees stopped their lunatic dance. The rain stopped when the last drop touched the ground. The moon shone more brightly."
n "The wind became silent. And the window was closed."
n "The entire scene was looking bizarre. How come everything became pin drop silent from stormy thunder?"
play music "break.wav"
scene bg white
with hpunch
"THADAAAAKKKK"
scene bg white
with hpunch
n "My heart skipped a beat. The entire window pane broke into million pieces and intense white light streamed from outside into my room, blinding me temporarily."
n "What was happening?- I asked myself with my eyes tightly shut."
stop music
scene bg broken
with fade
play music "eerie.mp3"
n "I slowly opened my eyes, trying to understand the situation."
n "The window was completely broken, and through the cavity of the window, I saw someone looking right at me."
n "Afraid, my mouth stumbled with words."
n "\"Wh-Who are y-you?\""
n "The face of the person was silhoutted by the bright beam of light coming behind them."
n "And my heart lurched when the person entered my room through the window."
n "\I- I WILL CALL THE COPS RIGHT NOW!!!\""
n "I tried shouting. I wanted to run away as fast as possible but a strange swoon froze me in my position. I myself wasn't letting go of me."
n "\"IF YOU TRY COMING NEAR ME, I WILL KILL YOU!\""
n "I knew I was sounding so stupid but I couldn't really think of anything else."
play music "creepy.mp3"
show entity
with zoomin
stop music
play music "eerie.mp3"
e "Humans, humans, humans."
e "All of them materialistic."
e "Cannot live without greed."
e "Cannot live without want. All you humans, are made of same matter. Selfishness."
n "The entity spoke very calmly but in a sardonic way."
n "\"WHO THE HELL ARE YOU!\""
e "I am someone who can grant you all your wishes."
n "I was stunned. At middle of the night, someone breaks into my house and speaks rubbish. This was clearly idiocy."
n "\"I am calling the cops. You are not going to do anything criminal in my house.\""
e "The house which is going to be mortgaged? And whose house? Yours? Who is soon destined to go bankrupt. Clearly not."
n "I was silent. Maybe she got to know about me beforehand. But the entire series of event from the heavy stormy rain to everything standstill."
n "And that weird white light. Something was really off."
e "I don't care about the questions in your mind, Raaha. I am here to give you what you want."
n "\"And why should I trust you? Who are you? How did you come here? Who told you about me?\""
e "I said no questions. Tonight, all your wishes will be fulfilled. Every incompleted wish which you yearn for."
n "I kept staring at her. What was she speaking?"
e "I am not lying. Each word of mine is true. I am here for your benefit."
e "Whoever accepts my proposal, they never regret to live. They get all the happiness of their life."
n "I was stunned."
n "Everything was moving in a spiral in my mind."
n "I had no idea what exactly was happening with me. I stood flabbergasted."
e "Oh come on, don't you have your wishes to be fulfilled? Get back your status in society? Become rich once again?"
n "Probably, I wanted all those things. But what authority did she have to bestow these on me?"
n "I chose not to speak anything."
e "Haha, you think too much, don't you? Thinking gives pain Raaha, only pain!"
n "And I promise you, I will relieve you of all your pains."
n "I stood staring into her eyes. Her eyes acted as a shield to know her real intentions."
e "Raaha, I am here to bestow upon you all the happiness you deserve. I am here to lead you to a better world, a world worthy of you."
e "You never feel unsatiated."
e "And if you are thinking why am I being so benevolent and offering such a golden opportunity. It is because-"
n "She paused."
n "\"Because what?\""
e "Because you opened the gateway for me, for us, for the Utopia."
e "And for yourself."
n "She spoke with a sly smile on her face."
n "This meant one thing - grandma was right all along. There exists a gateway for the unknown to enter our world through a window."
n "And this woman looking entity was offering me the luxuries of life. Riches, fame and what not."
n "And apparently, she didn't want anythiing in return, which seemed very weird."
n "Was it all real even?"
n "My head was puzzled with this. Was it something out of a Lovecraftian horror? The unknown. The forbidden knowledge. The secrets which we weren't supposed to know?"
n "I took a step back. I was afraid with whatever was happening in front of my eyes."
n "I was highly skeptical. A myth was coming true!"
e "Don't be afraid Raaha, I am here to help you. I am here to shower you all the comforts of your life which you deserve."
e "Don't you believe me?"
n "She spoke with a twinkle in her eyes."
e "My homeland is fulfilled with propserous men and women. It is a utopia of wonders."
e "No one is left unsatisfied in my world. It is billion times better than this Earth of yours."
n "I kept quiet."
e "Look at your world. Broken, dusted, shattered, polluted and poisoned. No man and no woman is happy. Everyone in your world is finding a gateway to escape their pain."
n "I silently looked at her red eyes."
e "My world will offer every desire of yours. You just have to say a yes. Walk right through this window and you will experience the mirth of your life."
e "No ifs and buts will help you live happily. It's your decision but remember, you would be missing a great deal tonight if you play your cards wrong."
e "Imagine the immense wealth, opulence, respect, love and power. Every wish of yours will be fulfilled."
n "I really wanted to believe each word of hers. I wanted happiness. I wanted everything back which I had lost."
menu:
        e "So what is your final decision?"

        "Yes":

         jump two_b

        "No":

         jump two_a_r

label two_a_r:
play music "scr.mp3"
scene bg entity2
with vpunch
e "WHAT DID YOU SAY, YOU LITTLE MINK!"
play music "terror.mp3"
n "My heart started pounding. The wind was raging like a beast. Thunder and lightning alternated in an erratic rhythm."
n "\"No. I don't trust you and this world of yours. My world is known to me, no matter how much pain I have received.\""
n "\"How- how can I believe you just like that? And all your claims?\""
n "I try to protest. I won't lie but yes, I am in two minds."
e "No Raaha, your world never gave you the respect you deserved. A temporary fame doesn't account for your value."
e "You deserve better. Each dream of yours will be the dream of the Utopia. And Utopia never disappoint anyone."
e "You will be in abundance, the Cornucopia will cater every need of yours and the people of Utopia will worship you as their Queen."
n "This sounded tempting and intriguing. Really, did such a world exist?"
n "What should I do? And what will be the consequence of my action?"
e "Don't ponder much poor girl. Your world is very small and hardly had anything offer."
e "On other hand, your crown awaits at the throne of the Utopian Kingdom. Everybody is waiting for your first step into the kingdom."
e "Doesn't that sound too tempting an offer?"
n "I stayed quiet but I was tempted."
n "After all, I was once the queen of my industry. The most hit author of the 21st century. Youth used to worship me."
n "But soon the flame of fans and supporters died, and the publishers began ignoring me, trashed my new manuscripts."
n "They said that my style had became outdated and the flair was gone. I was labelled as a \"prosaic writer\"."
n "I lost my fame and soon afterwards my wealth. I was going towards bankruptcy."
n "I wanted my respect back."
n "I felt I deserve that queen title and I need to get it back."
n "But trusting someone who just crashed into my home was difficult."
n "The entity looked enigmatic."
n "It was tough to know her true intentions."
n "And now, I had a choice to make."

menu:
     "What should I do?"

     "I am ready to go.":

        jump two_b_r

     "No, I shouldn't deter.":

        jump two_a_l

label two_b_r:
scene bg broken
show entity
with zoomin
play music "eerie.mp3"
e "Now that is what I call a perfect choice. Walk through this gateway and you will be the Queen of Utopia."
stop music
scene bg kingdom
play music "amb.mp3"
with fade
e "Come, walk slowly through the window, leaving all your earthly possesions, including your thoughts, to the place of perfection, of propersity."
e "You will have all the riches, all the wealth that you couldn never have imagined. It will be all yours. You buy happiness in my land."
e "You will never fall short of anything. The more you will want, the more you will get."
e "Everybody will be your slave. Your word, their duty."
e "No tension of poverty, no worry of losing fame. You will be at the top."
e "Go, join the gold rush!"
n "I came through the window and jumped into the other side."
n "As I walked into the new world, my eyes shone brightly."
n "The castle was made of solid gold and studded with diamond, pearls, emeralds, sapphires and rubies."
n "The people around the castle looked so beautiful and exotic. Their attire, their jewellery - everything was so lavish."
scene bg ins
with fade
n "I entered the castle. Its inside was also no less than a fairytale castle. Aesthetic, beautiful, rare decorations filled up the castle."
n "There were thousands of servants and slaves running errands. Smell of delicacies being cooked came from a grand kitchen."
n "Everything was so prosperous."
n "Opulence was another name for this world."
n "And I became their queen. They became my obedient subejcts. I felt the essence of being the most powerful. Like I used to be."
n "I got immersed in my bountiful life."
n "I forgot that Earth or the people there ever existed for me."
n "There was never shortage of anything."
n "Land of Utopia was my kingdom and I ruled over everyone. Everyone praised me and held me in high regards."
n "I began loving this new authority and enjoyed it as much as I could."
scene bg cru
with fade
play music "evil.ogg"
n "And soon, I had became arrogant with the power, greedy with the money and narcissist with my beauty. I became more and more self-conceited."
stop music
play music "ambe.ogg"
n "It was me, me and only me. The most powerful, the most beautiful and the richest. I had drowned myself in pride."
n "I got drunk by the immense power I held in my hands."
n "I was called a sybarite."
n "Opulence drenched me into gluttony."
n "And dried the goodness left inside me."
n "I stopped caring about my subjects. Their welfare hardly mattered to me."
n "My sense of greed prevailed over my sense of justice. I awarded punishments to the innocents, just the sake of money."
n "My sense of pride didn't let me nice to anyone. I mistreated everyone."
n "I gave immense trouble to everyone."
n "Greed of wealth, fame and power drove me mad."
n "I turned the utopia into a dystopia."
n "And the day of my end reached me quick."
scene bg burn
with hpunch
play music "Firescape.mp3"
n "The subjects, tired of my authority, decided to get rid of me."
n "They burnt my magnificent castle, with cries coming from outside, telling me one thing."
"This ain't the fire which we riot, this is the fire of your crime, this is the fire of your sins."
"You let your greed push you into our Utopia and see how it destroyed you."
"This is the punishment of your misdeed."
play music "scream.mp3"
n "And I shrieked in the fire of my guilt."
stop music
play music "terror.mp3"
n "I wish I had listened to my grandma's words."
n "Never leave the windows open at night."
n "Or the gateway to hell opens."
scene bg room1
with fade
play music "eerie.mp3"
"Bad Ending ~ Sanity overcame by Vanity"
stop music
scene bg cred
with dissolve
"Hope you all enjoyed the game! Do leave your reviews and feedbacks! Thanks for playing!"
return
label two_a_l:
scene bg entity2
with hpunch
play music [ "scr.mp3","terror.mp3"] fadeout 1.0 fadein 1.0
e "Hah! Trying to be noble in front of me?"
e "I know all your secrets. How you were left with a willow in your hand!"
n "I looked at her with shocked eyes."
e "Didn't your love left you?"
e "Oh! Rather you were the one to desert them, right?"
n "She asked with an evil grin."
n "It felt as if someone tore my old wounds."
n "She was talking about him."
n "My face drooped in a melancholic state. Tears started falling from my eyes."
e "Oh you don't worry sweetie, because I am here to make an offer."
e "An offer which you cannot refuse."
n "I looked at her. I didn't want to believe her words. Was she bluffing?"
e "Just say yes and he will be in front of you."
e "I can see the hidden desires of your heart."
e "Love is a beautiful feeling. Don't you wish to experience it again?"
n "She was right. Love is truly a beautiful feeling."
n "But I was scared and doubtful of her claim."
n "If he really came in front of me, what will he say? Will the situation become awkward?"
n "I shook my head, trying to decide."
e "Don't think too much Raaha. A \"Yes\" will be enough."
n "Emotionally, I was feeling inclined to say yes. But my rational mind was trying to resist."
n "What should I go for? - The heart or the mind?"
menu:
    "Do you want him back?"

    "Yes":

       jump two_b_l

    "No":

       jump two_a_f

label two_a_f:
scene bg entity2
with hpunch
play music "scr.mp3"
e "HOW ADAMANT YOU ARE, YOU HOG!"
play music "scrhor.mp3"
e "Listen you damned dalmatian, you opened the gateway to Utopia and now you are rejecting its offer! A very very tempting offer."
play music "eerie.mp3"
n "The entity spoke in her most alluring voice."
e "Why don't you give in already? You will give up eventually."
e "Because you don't have the spine to stand up for yourself. You pretended all your life you were selfish but in reality.."
e "We all know who you are. A coward, who lost every time, and eventually lost all the people who loved her."
e "Because you never had the power of handling things. You have always been a loser."
e "The only people who could accept you was your family. A sweet big family. Whom you deserted years ago."
n "I flinched. That was the most fatal attack from her."
e "Hah! What happened? Feeling offended?"
e "But as I said, my offer will give you unlimited peace and happiness. You will never have to cry on your pillow again."
n "I looked at her."
e "I will return you the most part of your life. Your family. Step into this window which will serve as the gateway to your home sweet home."
n "I definitely missed my family. How often I wished that I was with them, sharing my success with them. But none of them happened. I left home."
n "And so did home. They never tried to contact me ever nor responded to my futile tries."
n "I was getting an opportunity to be with them. Reconnect with them."
n "But trusting this entity and the window was still difficult."
menu:
    "Make a move which you won't regret."

    "Yes, I want my family back.":

       jump two_b_f

    "No, I don't need a gateway to fulfill my desires.":

       jump two_a

label two_b_l:
play music "rom1.ogg"
scene bg luv
n "The window showed a garden in which variety of greenery filled up the place."
n "As I saw across the lush green, there was a glass wall behind which someone was standing."
n "Their face was hidden by the branches and the reflected sunlight."
n "But as I stared more into the garden and its elements, I realised who the person was."
n "It was him."
n "He. For whom, my heart burnt itself a thousand times."
e "Do you see him?"
n "I kept gazing at the wonder sight on the other side of the window."
e "Love came at no cost but it was lost for a great amount of cost."
n "I knew what the entity was hinting at."
e "Don't think too much, you wanted your love back, didn't you?"
n "I was in a fix. I wanted him so bad in my life, even after the emotional torture I had to bear."
n "Because, somewhere my heart still loved him."
n "I took a step and climbed over the window."
play music "rom2.ogg"
n "And jumped into the garden. In the garden, he was still talking over his cellphone. I snatched it away and with tears in my eyes, I said-"
n "\"Still no time for this poor girl?\""
n "He looked at me and was shocked."
l "Raaha?"
n "My heart bursted with excitement. He acknowledged my presence!"
n "\"Love, I am so sorry I left you over that misunderstanding. I miss you so much. Words will fall short in expressing how much I love you.\""
n "My mind was racing with the memories we had made a few years ago."
n "It was all sweet and bright till the point I started getting suspicious about his activities. I thought he was going far away from me."
n "We used to fight a lot. He called me obsessive and possessive. I used to get even more angry on listening to his words."
n "Unfortunately, we had to part our ways. But I regretted each word that I spoke and repented his loss."
n "I badly wanted him back in my life and now here's my chance."
n "\"Will you forgive me?\""
n "He looked at me with a confused look. But in a minute, his face broke into a smile and he opened his arms."
scene bg hug
with slideright
n "I ran into his arms, hugging him like a monster, kissing him on his cheeks, on his neck."
n "I held him tightly, so that this time I wouldn't let go of him."
n "He's mine. And forever mine."
play music "ambe.ogg"
n "But who knew, we both were right. That I was obsessive and possessive."
n "And he, a cheat."
n "With days passing by, we kept loving each other, promising each other never to leave again, all merry in our life."
n "But I got to know, it was a facade. He was with me because I was like a bank to him."
n "He played with my emotions to satisfy his love's heart, which wasn't mine."
n "My obsession for him had reached the zenith. I couldn't tolerate the fact that he belonged to someone else."
n "HE ONLY BELONGED TO ME."
n "And that he cheated on me for my money."
n "While at the same time, he gaslighted me for being workaholic and money-minded."
n "That was the reason I had left him, because I put my career first."
n "But now, I finally understood his drama."
n "And my heart couldn't take that."
scene bg knife
with blinds
n "So, it was time to lay him to rest."
n "Like how he softly choked my feelings."
n "I smiled at him and proceeded to hug him."
n "With a knife in my hand."
play music ["stab.mp3","man.mp3"] fadein 1.0 fadeout 1.0
n "And I stabbed him. I kept stabbing him at various part of his body till my raging heart was quiet."
n "His action led me to this gateway."
stop music
n "I wasn't at fault, but I was overloaded with emotions."
n "And unable to relieve myself of guilt from killing him, rather, loving him.."
play music "stab2.mp3"
n "I stabbed myself in the end."
play music ["aah.mp3", "terror.mp3"] fadein 1.0 fadeout 1.0
n "Before closing my eyes, I remembered the window and the entity for the one last time."
n "And what my grandma used to say.."
n "Never leave the window open at night."
n "Or a gateway to destruction will open."
stop music
scene bg room1
with fade
play music "eerie.mp3"
"Bad Ending ~ \"Find what you love and let it kill you\""
stop music
scene bg cred
with dissolve
"Hope you all enjoyed the game! Do leave your reviews and feedbacks! Thanks for playing!"
return
label two_b_f:
scene bg broken
show entity
e "I knew you would succumb to my offer."
e "Everyone loves their family, no matter how they are themselves or how their family is."
e "Isn't it Raaha?"
n "I chose not to react on her question."
e "Now, slowly walk through this portal to meet your loved ones whom you had been missing since an eternity."
scene bg out
with fade
e "Climb the window and jump into my Utopia, where you will find them."
n "I looked at the window. The nightsky had turned lighter a shade."
scene bg black
n "I went through the window and found myself in a room."
play music "amb.mp3"
scene bg room3
with fade
n "It looked like a very known place. The shelves, the study table, the bed..."
n "Was it my room?"
n "I couldn't believe that I was finally back in my room after so many years."
n "Tears fell off my eyes. Was it all real?"
n "I wandered around my room, checking each item and component, reminiscing those days when I was writing my first novel."
n "My family wasn't supportive about my idea of making a career in writing."
n "So, I left my home, deciding to prove myself right."
n "But in the process, we grew very distant."
n "They didn't accept me back. They were still mad at me."
n "But will they accept me now? Or will I be still disowned?"
n "I looked at the photograph hung on my wall."
scene bg family
with fade
n "It was a family picture. Of my parents, grandparents and my siblings."
n "I was standing with grandma and my oldest brother was standing with Dad. Isa, my sister was with mom."
n "We had captured this picture when we went out for a picnic in the winters. Dad had got a promotion and hence we decided to have a picnic party."
n "But my plans weren't aligned."
n "I had planned to run away the same day."
n "Because my family wasn't letting me pursue my passion. And I had got a great deal with a reputed publishing company to publish my first novel."
n "Now thinking about it, I feel bad. Maybe I could have convinced them. Running was a bad choice."
n "..."
n "How happy we all were together!"
n "I looked at the door of my room. Maybe, my family is in the living room, laughing and enjoying."
n "Do they even remember me?"
n "They never responded to my messages and calls when I climbed the ladder of success."
n "I missed them. But now, I was here. To mend ties."
n "What would be their reaction on seeing me?"
n "Honestly, it felt a bit overwhelming."
n "So many emotions were running in my brain."
n "But slowly, I took steps towards my door to open it."
play music "creak.wav"
scene bg sis
n "When suddenly, a creak sound echoed and I saw Isa, my sister."
stop music
play music "amb.mp3"
n "Expectedly, she looked at me as if she saw a ghost and ran to the living room. Definitely, she was going to tell everyone that I am back."
n "I was nervous, thinking what could happen next."
n "Soon, Isa came running to me, panting."
i "You are really my sister, aren't you?"
n "I nodded."
i "You're back?!"
n "I stayed still."
n "Isa scanned me from top to bottom and looked into my eyes."
i "Nobody's believing me. Come with me, comee."
n "Isa pulled my hand as hard as she could and brought me straight in the living room."
scene bg fm
with dissolve
i "See, I wasn't bluffing. She's for real."
n "My entire family stared at me. There were new faces also mixed with my family members. They were also looking stunned, seeing me."
g "Raaha?"
n "I couldn't hold myself back and sprang towards grandma, closing her into a tight hug."
scene bg hg
with fade
n "Grandma, I am so sorry."
n "Grandma caressed my back and my head."
n "I just wanted to pursue my passion. Nothing else. I love you all so much. I am sorry about what I did earlier."
g "It's alright sweetie, now that you are back, we won't let you go."
n "I looked at grandma. She wore a sad smile on her face."
g "Isa, take Raaha back to her room."
n "Isa nodded and asked me to walk with her. I saw the looks of my other family members. They didn't seem as happy as grandma."
n "Maybe they were still angry at me. But I know, their heart would melt soon."
scene bg room3
with fade
n "I went inside my room and Isa stood staring at the wall with a grim expression."
scene bg wall
with fade
stop music
n "Then I turned back. The window through which I had come into the room - it had vanished!"
n "\"How did that happen?!\""
scene bg scare
with vpunch
n "I asked in shock."
play music "spooky.mp3"
i "That's what you pay for keeping the window open at night."
n "No, I didn't hear correctly, did I?"
n "What was Isa speaking?"
i "But now you are back, we will make sure you NEVER escape again."
n "Isa spoke with a villainous smile."
n "\"ISA!?\""
scene bg knob
n "I got scared listening to her such words."
play music "close.mp3"
n "As I took a step towards her, she quickly went outside the room and closed the door."
stop music
n "I tried opening the door but it was locked."
n "I looked around my surroundings, there was no escape. The window was gone, the door locked and it was only me in the room."
n "I felt scared and alarmed. Something wasn't right."
play music "bang.mp3"
n "I banged the door and shouted."
n "\"ISA OPEN THE DOOR. WHY DID YOU LOCK ME IN? OPEN UP!"
i "So that you don't run away again."
n "I heard Isa's voice from the other side."
g "Is she properly caged? Windows are properly sealed or not?"
stop music
play music "spooky.mp3"
n "That voice was of ..."
n "...of Grandma?"
n "\"Grandma, is that you? Grandma, please get me out of here. I don't know why Isa is doing this.\""
g "I told her to do so."
n "\"But- but why ?\""
g "I think you forgot my words, Raaha."
g "Never leave the windows open at night."
g "Or else, you have to pay a big price."
g "By giving away your control over your own life."
g "By losing your identity, your character."
g "Now, I cannot let you do so Raaha, after all you are my favourite."
g "So, it is better if we keep you caged inside a room without any windows. You will be protected and safe."
n "I was not able to believe what Grandma was saying. Locking me inside with no windows just for my safety?"
g "You have a tendency of running away from all situations, right?"
g "This time, no running, only staying, in one place. FOREVER."
n "It wasn't grandma's voice. Someone else was speaking. This entire thing was fake. This wasn't my family. I had been tricked."
play music "cry.mp3"
scene bg given
n "I cried hard to get out of there. But no one responded after that. I kept banging the door, scratched the wall like a lunatic to find the window."
n "But all turned futile, I knew my bed was going to be my deathbed."
play music "eerie.mp3"
scene bg sad
n "I laid on my bed, closing my eyes and calmly remembering Grandma. My real grandma."
n "As she used to say."
play music "terror.mp3"
n "\"Never leave the window open at night. Or else-\""
n "Gateway to delusion opens."
play music "eerie.mp3"
scene bg room1
"Bad Ending ~ Utopia : Far From Home"
stop music
scene bg cred
with dissolve
"Hope you all enjoyed the game! Do leave your reviews and feedbacks! Thanks for playing!"
return
label two_b:
scene bg broken
play music "eerie.mp3"
show entity
e "Ah, a quick and right decision."
e "So now, place your steps in the Utopia."
e "Imagine the Utopia you wished to see and across the window, you will find one."
e "I assure you, you won't be disappointed."
n "I was fed up of the life I was living. I wanted good things back."
n "And I had a feeling maybe I could trust this entity."
n "If she could come from the gateway through the window, there must be a way to go the Utopian land."
n "And gain all the wealth, fame and love I had craved for."
n "All my wishes would get fulfilled. There won't be any tension, any worry, any anxiety."
n "Only happiness."
scene bg open
n "I listened to the entity and jumped out of my window."
scene bg black
n "But it was all my hallucination."
play music "aah.mp3"
scene bg red
with vpunch
n "I fell to my death from the second floor of my apartment."
stop music
scene bg black
play music "terror.mp3"
n "There was no entity, no gateway."
n "Before taking my last breath, I realised how greedy and self conceited I had been."
n "Greed drove me to leave my home. Greed made me leave my love."
n "And now, greed killed me."
n "I am not sure what I saw through the window"
n "But it felt so real that I got controlled by the hallucination."
n "I remembered my grandma's words."
n "Never leave the window open at night."
n "Or else, a gateway to illusion opens."
scene bg room1
play music "eerie.mp3"
"Bad Ending ~ \"Earth provides enough to satisfy every person's needs, but not every person's greed\""
stop music
scene bg cred
with dissolve
"Hope you all enjoyed the game! Do leave your reviews and feedbacks! Thanks for playing!"
return
label two_a:
scene bg broken
with dissolve
show entity
play music "amb.mp3"
e "Oh, I see."
e "You remained unaffected by the greed, by the lust, by the seven sins which can destroy anyone."
e "You are strong enough to tackle your own problems, without letting them overcome you."
e "You will always find a way."
e "Guess what, I had only three chances. And now, it is my time to leave."
e "Good luck with your world."
e "But, if you ever feel like taking a taste of the Utopian Land."
e "Just keep the windows open at night."
e "I will be there."
n "She spoke with an uncanny smile and suddenly, the wind started raging."
play music "rainwin.wav"
n "Everything started flying here and there, the trees started swaying, the rain grew heavier."
n "Lightning and thunder rambled the sky."
n "Again that strange white light flashed through my eyes, temporarily blinding me."
play music "scrhor.mp3"
scene bg white
with hpunch
scene bg black
with hpunch
scene bg red
with hpunch
e "Au revoir!"
scene bg white
with hpunch
stop music
play music "amb.mp3"
scene bg room2
with fade
n "And once again, everything fell silent."
n "Nobody was in my room."
n "My eyes fell on the window."
n "It was completely fine and closed."
n "As if it were never broken or opened."
n "I stood near the window and contemplated."
n "My grandma was always right. She indirectly saved me from something abysmal."
n "Grandma used to tell me, how entities would come if the windows weren't closed properly at night."
n "The window served as the gateway for them to interact with us."
n "The entities would try their best to evoke our vulnerable side and push us to commmit any of the seven sins."
n "So that we get trapped in their world, which was on the other side of the window."
n "They would trouble the human trapped in the virtual reality of their so-called Utopia till the human killed itself."
n "And then, they would feast on the soul of the human."
n "Making them stronger and more convincing."
n "It was difficult for me to resist the entity's charms and claims."
n "Because, she fished in the troubled waters. She tried using my weak spots and vulnerability to convince me."
n "But I remembered Grandma's words."
n "Never listen to the people of the gateway."
n "Otherwise, you will lose yourself."
n "I am thankful to grandma for her advice."
n "And surely, I will keep the windows closed at night."
scene bg room1
with fade
"Good Ending ~ Escaped the Gateway"
scene bg cred
with fade
"Hope you all enjoyed the game! Do leave your reviews and feedbacks! Thanks for playing!"
return
label one_a:
scene bg window6
play music "softrain.mp3"
n "I was not being superstitious. But I wasn't really in a mood to do anything."
n "I had lost the will to try something new or experiment."
n "Life had tested me at every moment of my life."
n "No energy was left inside me."
n "I just wanted to sleep."
n "Sleep peacefully. And maybe forever."
n "I closed the window lest anyone could peep what I am upto."
n "I am not sure whether it is a good ending for me, but at least, it will be an end to my suffering."
n "I look at the window for the one last time before proceeding to sleep."
"Not so good ending ~ Eternal Sleep"
stop music
scene bg black
with fade
scene bg cred
"Hope you all enjoyed the game! Do leave your reviews and feedbacks! Thanks for playing!"
