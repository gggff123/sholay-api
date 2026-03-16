
story=["""
Jai and Veeru are small-time crooks who are released from prison, where they are recruited by a former Inspector Thakur Baldev Singh to capture a notorious dacoit named Gabbar Singh wanted for ₹50,000, as the duo had saved Thakur from a train robbery, which makes Thakur recruit them for the mission with an additional ₹20,000 reward. The duo leaves for Thakur's village in Ramgarh, where Gabbar is residing and terrorising the villagers.
After reaching Ramgarh, Veeru falls for Basanti, a feisty, talkative horse-cart driver. Jai meets Thakur's widowed daughter-in-law, Radha, and falls for her; she later reciprocates his feelings. The two thwart Gabbar's dacoits, who came to extort money and goods. Later on, the three dacoits, including Kaalia, are killed by Gabbar. During the festival of Holi, Gabbar's gang attacks the villagers, where they corner Jai and Veeru, but the duo manage to attack and chase them away from the village. The duo is upset at Thakur's inaction (when Jai and Veeru were cornered, Thakur had a gun within his reach, but did not help them) and considers calling off the mission. Thakur reveals that a few years ago, Gabbar had killed his family (save for Radha and Ramlal), and had both his arms cut off; he concealed the dismemberment by always wearing a shawl, the sole reason he could not use the gun.
Realising how much Thakur has suffered, Jai and Veeru take pity by taking an oath that they will capture Gabbar alive, free of charge. After learning the duo's heroics, Gabbar kills Ahmed, the local imam Rahim Chacha's son, to threaten the villagers to make Jai and Veeru surrender to him. The villagers refuse and instead get the duo to kill a few of Gabbar's henchmen in revenge for the boy's death. Gabbar angrily retaliates by having his men capture Veeru and Basanti. Jai arrives and attacks the hideout, where the trio can flee Gabbar's hideout with dacoits in pursuit. Shooting from behind a rock, Jai and Veeru nearly run out of ammunition. Unaware that Jai was wounded in the gunfight, Veeru is forced to leave for more ammunition and also to drop Basanti at a safe place.
Jai sacrifices himself by using his last bullet to ignite dynamite sticks on a bridge from close range, killing Gabbar's men. Veeru returns, and Jai dies, leaving Radha and Veeru devastated. Enraged, Veeru attacks Gabbar's den and kills his remaining men, where he catches Gabbar and nearly beats him to death. Thakur appears and reminds Veeru of the vow to hand over Gabbar alive. Thakur uses his spike-soled shoes to severely injure Gabbar and his hands. As Thakur is about to kill Gabbar, the police arrive, and the senior officer convinces Thakur to let go, explaining that he was also a police officer, whose example is legendary. Convinced, Thakur lets go, and the police arrest Gabbar for his crimes.
After Jai's funeral, Veeru decides to leave Ramgarh, with Thakur empathising with him. After boarding the train, he finds Basanti waiting for him on the train, and they both embrace each other.
Director's cut : The original director's cut has a different ending. The police do not arrive to stop Thakur. Instead, he kicks Gabbar onto a nail on one of the two poles that Gabbar had used to chain Thakur when he had cut off his arms, thus stabbing him in the back and killing him. This version also has deleted scenes that include Thakur's shoe soles getting laced with spikes, the scene in which Thakur's family is massacred, and the scene in which the imam's son is killed (all of which were originally cut by India's Censor Board).[8] The Censor Board was concerned about the violence, and that viewers may be influenced to violate the law by punishing people severely.Although Sippy fought to keep the scenes, he ultimately had to reshoot the ending, and as directed by the Censor Board, have the police arrive just before Thakur can kill Gabbar.
"""]
cast=[
"Dharmendra as Veeru"
"Sanjeev Kumar as Thakur Baldev Singh, a retired Police Officer",
"Hema Malini as Basanti, Veeru's love interest",
"Amitabh Bachchan as Jaidev 'Jai'",
"Jaya Bhaduri as Radha, Thakur's daughter-in-law and Jai's love interest",
"Amjad Khan as Gabbar Singh, a wanted dacoit.",
"A. K. Hangal as Rahim Chacha, the imam in the village",
"Satyen Kappu as Ram Lal, Thakur's servant",
"Iftekhar as Inspector Khurana, Radha's Father",
"Leela Mishra as Mausi, Basanti's maternal aunt",
"Vikas Anand as Jailor",
"Mac Mohan as Sambha, Gabbar Singh's sidekick",
"Keshto Mukherjee as Hariram, prison barber and Jailor's side-kick",
"Sachin Pilgaonkar as Ahmed, son of the imam",
"Master Alankar as grandson of Thakur Baldev Singh; the character's name is not mentioned in the film.",
"Viju Khote as Kaalia, one of the Gabbar's men whom he kills in a game of Russian roulette",
"Major Anand as unnamed, one of the Gabbar's men whom he kills in a game of Russian roulette",
"Bhagwan Sinha as unnamed, one of the Gabbar's men killed by him in a game of Russian roulette",
"Arvind Joshi as elder son of Thakur Baldev Singh",
"Bhanumati as Nirmala",
"Birbal as the prisoner with half shaven mustache",
"Raj Kishore as a jail inmate with gayish mannerisms",
"Asrani as the Jailor, a comical character modelled after Charlie Chaplin in The Great Dictator",
"Gita Siddharth as Geeta, Thakur Baldev Singh's daughter in law",
"Helen in a special appearance in song 'Mehbooba Mehbooba'",
"Jairaj as Police Commissioner",
"Jagdeep as Soorma Bhopali, a comical wood trader",
"Jalal Agha in a special appearance in song 'Mehbooba Mehbooba'",
"Om Shivpuri as a police officer investigating Gabbar's attack in the village.",
"Sharad Kumar as Ninni, younger son of Thakur Baldev Singh"
]
realease=["15 August 1975"]
dis=["sippy films"]
dire=["G P Sippy"]
img=["https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Sholay-poster.jpg/250px-Sholay-poster.jpg"]
#IMPORTS
from flask import Flask,render_template
app=Flask(__name__)
#HOMEPAGE
@app.get("/")
def home():
    return "THE SHOLAY API . VISIT DOCS FOR MORE --2026--"
@app.get("/get-all")
def all():
    return {"Story":story,"Cast":cast,"release-date":realease,"Distributed by":dis,"Director":dire,"Poster-image":img}
@app.get("/docs")
def docs():
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)