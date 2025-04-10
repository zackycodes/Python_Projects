import time
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Voice changer

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Functions; choose as per conveniece


def say_script(script):
    engine.say(script)
    engine.runAndWait()

def dictating_bot(script):
    words = script.split()
    i = 0
    while i < len(words):
        # Get the next 5 words
        chunk = words[i:i+5]
        sentence = " ".join(chunk)
        
        # Speak the 5 words
        engine.say(sentence)
        engine.runAndWait()

        # Repeat the last 2 words (if there are at least 2)
        if len(chunk) >= 2:
            repeat_words = " ".join(chunk[-2:])
            engine.say(repeat_words)
            engine.runAndWait()
        
        # Wait for 1 second
        time.sleep(1)
        
        # Move to the next 5 words
        i += 5

# ---------------------------------------------------------#

# Scripts
# Key syntax: code <sub>, <n>

h_1 = ""
h_2 = ""
h_3 = ""
h_4 = ""
h_5 = ""


c_1 = ""
c_2 = ""
c_3 = ""
c_4 = ""
c_5 = """  Unification of Germany
1. In 1848 Germans tried to unite the different regions of the German confederation into a
nation-state governed by an elected parliament. This liberal initiative to nation-building was,
however, repressed by the combined forces of the monarchy and the military, supported by
the large landowners (called Junkers) of Prussia.
2. Prussia’s chief minister, Otto von Bismarck, was the architect of unification process which
was carried out with the help of the Prussian army and bureaucracy.
3. Three wars over seven years – with Austria, Denmark and France – ended in Prussian victory
and completed the process of unification.
4. In January 1871, the Prussian king, William I, was proclaimed German Emperor in a
ceremony held at Versailles.
5. The nation-building process in Germany had demonstrated the dominance of Prussian state
power. The new state placed a strong emphasis on modernising the currency, banking, legal
and judicial systems in Germany. Prussian measures and practices often became a model for
the rest of Germany.
Unification of Italy
1. Italy was divided into seven states, of which only one, Sardinia-Piedmont, was ruled by an
Italian princely house. The north was under Austrian Habsburgs, the centre was ruled by the
Pope and the southern regions were under the domination of the Bourbon kings of Spain.
2. During the 1830s, Giuseppe Mazzini formed a secret society called Young Italy and
organized two revolutions for the unification of Italy but failed.
3. Sardinia-Piedmont under its ruler King Victor Emmanuel II took initiative to unify the Italian
states through war. Cavour, the Chief Minister of Sardinia-Piedmont led the movement to
unify the regions of Italy was neither a revolutionary nor a democrat.
4. Through a tactful diplomatic alliance with France engineered by Cavour, Sardinia-Piedmont
succeeded in defeating the Austrian forces in 1859 and captured north.
5. Apart from regular troops, a large number of armed volunteers under the leadership of
Giuseppe Garibaldi joined the fray. In 1860, they marched into South Italy and the Kingdom
of the Two Sicilies and succeeded in winning the support of the local peasants in order to
drive out the Spanish rulers. In 1861 Victor Emmanuel II was proclaimed king of united
Italy.

Unification of Britain and its strange way for unification
1. There was no British nation prior to the eighteenth century. The primary identities of the
people who inhabited the British Islands were ethnic ones – such as English, Welsh, Scot or
Irish. All of these ethnic groups had their own cultural and political traditions. But the
English nation was wealthy and powerful.
2. The English parliament, which had seized power from the monarchy in 1688 at the end of a
protracted conflict, was the instrument through which a nation-state, with England at its
centre, came to be forged.
3. The Act of Union (1707) between England and Scotland that resulted in the formation of the
‘United Kingdom of Great Britain’. England was able to impose its influence on Scotland.
English members dominated the British parliament, Scotland’s distinctive culture and
political institutions were systematically suppressed, Catholic clans of Scottish Highlands
suffered terrible repression, Scottish Highlanders were forbidden to speak their Gaelic
language or wear their national dress and large numbers were forcibly driven out of their
homeland.
4. Ireland suffered a similar fate. It was a country deeply divided between Catholics and
Protestants. The English helped the Protestants of Ireland to establish their dominance over a
largely Catholic country. Catholic revolts against British dominance were suppressed.
5. After a failed revolt led by Wolfe Tone and his United Irishmen (1798),Ireland was forcibly
incorporated into the United Kingdom in 1801.A new ‘British nation’ was forged through the
propagation of a dominant English culture. The British flag, the national anthem, the English
language – were actively promoted and the older nations survived only as subordinate
partners in this union.


"""










e_1=""
e_2=""
e_3=""
e_4=""
e_5="" 


g_1 = ""
g_2 = ""
g_3 = ""
g_4 = ""
g_5 = ""



# while True:
#     ask= input('Dictation or Say? (d/s) ').strip().lower()
#     if ask == 'd':
#         d_ask=input('Input key: ')
        
#         dictating_bot(d_ask)
#     elif ask =='s':
#         s_ask=input('Input key: ')
#         say_script(s_ask)

#     elif ask=="exit":
#         break
#     else:
#         print('Invalid function! please try d or s')



say_script(c_5)






