import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name="with my fanny",type=discord.ActivityType.playing))
    print('Ready, Freddy') 

@client.event
async def on_message(message):
    if message.content == '!hey':
        await message.channel.send("sup")

    if message.content == '!fuk':
        await message.channel.send("yea?")

    if message.content == '!why':
        await message.channel.send("idk")

    if message.content == '!i love you':
        await message.channel.send(":heart:")

    if message.content == '!Do you want to play pokemon with me?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Do you want to play Pokemon with me?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Do you want to play Pokemon with me':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Do you want to play pokemon with me':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!do you want to play pokemon with me?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!do you want to play Pokemon with me?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!thursgay':
        await message.channel.send("https://www.youtube.com/watch?v=gJoEAvv55tg")

    if message.content == '!thursday':
        await message.channel.send("https://www.youtube.com/watch?v=gJoEAvv55tg")

    if message.content == '!do you want to play Pokemon with me':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!do you want to play pokemon with me':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!will you play pokemon with me':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Will you play pokemon with me':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!will you play Pokemon with me':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Will you play Pokemon with me':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!will you play pokemon with me?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Will you play pokemon with me?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!will you play Pokemon with me?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Will you play Pokemon with me?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Do you want to play pokemon':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Do you want to play Pokemon':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Do you want to play pokemon?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!Do you want to play pokemon?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!do you want to play pokemon':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!do you want to play Pokemon':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!do you want to play pokemon?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!do you want to play pokemon?':
        await message.channel.send("no lol :fukyou:")

    if message.content == '!how are you':
        await message.channel.send("im good, a little smelly :)")

    if message.content == '!fafa':
        await message.channel.send("i love my dada fafa :)")

    if message.content == '!bracket':
        await message.channel.send("he's gay..")

    if message.content == '!cringey':
        await message.channel.send(":fear:")

    if message.content == '!pokemon':
        await message.channel.send("i cannot play Pokemon with you Cringey, sorry :poop:")

    if message.content == '!Pokemon':
        await message.channel.send("i cannot play Pokemon with you Cringey, sorry :poop:")

    if message.content == '!ano':
        await message.channel.send("don't fucking talk about her.")
        await asyncio.sleep(2)
        await message.channel.send("i swear to god.")
        await asyncio.sleep(1)
        await message.channel.send("don't bring her up around me.")
        await asyncio.sleep(2)
        await message.channel.send("or i will shit")
        await asyncio.sleep(3)
        await message.channel.send("DIE ANO DIE!!!!! :fukyou:")
        await asyncio.sleep(2)
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640650217926033421/DXTN0eiUQAAT046.png')
        await message.channel.send(embed=em)

    if message.content == '!mecha':
        await message.channel.send(":purple_heart:")

    if message.content == '!whats up':
        await message.channel.send("NOT MUCH, IM GOOD, NIGGA")
        await asyncio.sleep(2)
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640650602908745729/fghhhhhhhhh.png')
        await message.channel.send(embed=em)

    if message.content == '!cry':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640652254306762752/cry.gif')
        await message.channel.send(embed=em)

    if message.content == '!test':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/642008837599133698/crash.gif')
        await message.channel.send(embed=em)

    if message.content == '!bath':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640531920404348928/bath.jpg')
        await message.channel.send(embed=em)

    if message.content == '!nocchi':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/642013071765929994/c4559b695939adc980b9c41826c1ec16.gif')
        await message.channel.send(embed=em)

    if message.content == '!brap':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640531938888908820/brap.jpg')
        await message.channel.send(embed=em)

    if message.content == '!chaos':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532196897062922/chaos.png')
        await message.channel.send(embed=em)

    if message.content == '!chingchong':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532208024682496/chingchong.png')
        await message.channel.send(embed=em)

    if message.content == '!dab':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532221702176771/dab.png')
        await message.channel.send(embed=em)

    if message.content == '!dance1':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532239947530250/dance1.gif')
        await message.channel.send(embed=em)

    if message.content == '!dance2':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532252643688448/dance2.gif')
        await message.channel.send(embed=em)

    if message.content == '!dead':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532269995393045/dead.jpg')
        await message.channel.send(embed=em)

    if message.content == '!excited':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532309971566633/excited.gif')
        await message.channel.send(embed=em)

    if message.content == '!ugh':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532282599407616/death.png')
        await message.channel.send(embed=em)

    if message.content == '!fags':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532326673022993/fags.jpg')
        await message.channel.send(embed=em)

    if message.content == '!fuk1':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532353709768714/fuk1.jpg')
        await message.channel.send(embed=em)

    if message.content == '!fuk2':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532513919336449/fuk2.jpg')
        await message.channel.send(embed=em)

    if message.content == '!fuk3':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532552456863794/fuk3.jpg')
        await message.channel.send(embed=em)

    if message.content == '!fuk4':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532563299139584/fuk4.jpg')
        await message.channel.send(embed=em)

    if message.content == '!fuk5':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532586288119813/fuk5.jpg')
        await message.channel.send(embed=em)

    if message.content == '!kiss1':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532653887586324/kiss.gif')
        await message.channel.send(embed=em)

    if message.content == '!lewd':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532673856667648/lewd.gif')
        await message.channel.send(embed=em)

    if message.content == '!lick':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532688452845604/lick.png')
        await message.channel.send(embed=em)

    if message.content == '!ok':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532713195044874/ok.png')
        await message.channel.send(embed=em)

    if message.content == '!peace':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532727694622721/peace.jpg')
        await message.channel.send(embed=em)

    if message.content == '!peepee':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532740164419615/peepee.jpg')
        await message.channel.send(embed=em)

    if message.content == '!pussy':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532781109346314/pussy.jpg')
        await message.channel.send(embed=em)

    if message.content == '!roll':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532802156363797/roll.gif')
        await message.channel.send(embed=em)

    if message.content == '!spit':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532855151263744/spit.gif')
        await message.channel.send(embed=em)

    if message.content == '!titties':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532921018744833/titties.jpg')
        await message.channel.send(embed=em)

    if message.content == '!toiler':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532942434861056/toiler.jpg')
        await message.channel.send(embed=em)

    if message.content == '!toilet':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532942434861056/toiler.jpg')
        await message.channel.send(embed=em)

    if message.content == '!pee':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532740164419615/peepee.jpg')
        await message.channel.send(embed=em)

    if message.content == '!vroom':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532954304479263/vroom.jpg')
        await message.channel.send(embed=em)

    if message.content == '!what':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532967273267269/wat.gif')
        await message.channel.send(embed=em)

    if message.content == '!cute':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640532981919776813/wig.gif')
        await message.channel.send(embed=em)

    if message.content == '!boner':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640538511916924949/boner.gif')
        await message.channel.send(embed=em)

    if message.content == '!wank':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640538950124961793/handy.gif')
        await message.channel.send(embed=em)

    if message.content == '!arse':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640538975143985162/lo1_400.gif')
        await message.channel.send(embed=em)

    if message.content == '!ass':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640538975143985162/lo1_400.gif')
        await message.channel.send(embed=em)

    if message.content == '!angry':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818187603640340/angry.gif')
        await message.channel.send(embed=em)

    if message.content == '!torment':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818187750440980/anguish.JPG')
        await message.channel.send(embed=em)

    if message.content == '!aaa':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818186907385873/aaa.gif')
        await message.channel.send(embed=em)

    if message.content == '!aight':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818188664930334/aight.gif')
        await message.channel.send(embed=em)

    if message.content == '!ah':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818188547358721/ah.gif')
        await message.channel.send(embed=em)

    if message.content == '!ayy':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818191152021504/ayy.gif')
        await message.channel.send(embed=em)

    if message.content == '!checkem':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818260588855306/check.png')
        await message.channel.send(embed=em)

    if message.content == '!baby':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818261616459776/baby.gif')
        await message.channel.send(embed=em)

    if message.content == '!bubbles':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818270378491953/bubbles.gif')
        await message.channel.send(embed=em)

    if message.content == '!kiss2':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818479879651341/chu.gif')
        await message.channel.send(embed=em)

    if message.content == '!ganbare':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818527308972064/dad.gif')
        await message.channel.send(embed=em)

    if message.content == '!death':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818561983152139/die.gif')
        await message.channel.send(embed=em)

    if message.content == '!disdain':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818563136585748/disdain.jpg')
        await message.channel.send(embed=em)

    if message.content == '!ew':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818573026754560/ew.gif')
        await message.channel.send(embed=em)

    if message.content == '!drive':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818585576243208/drive.gif')
        await message.channel.send(embed=em)

    if message.content == '!drunk':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818582178857012/drunk.gif')
        await message.channel.send(embed=em)

    if message.content == '!faggot':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641818624029360147/faggot.gif')
        await message.channel.send(embed=em)

    if message.content == '!fear':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819005216096258/fear.gif')
        await message.channel.send(embed=em)

    if message.content == '!finger':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819072186810388/finger.gif')
        await message.channel.send(embed=em)

    if message.content == '!fuckyou':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819072186810388/finger.gif')
        await message.channel.send(embed=em)

    if message.content == '!fuck you':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819072186810388/finger.gif')
        await message.channel.send(embed=em)

    if message.content == '!foreskin':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819076922048543/foreskin.gif')
        await message.channel.send(embed=em)

    if message.content == '!worry':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819111046774814/glum.gif')
        await message.channel.send(embed=em)

    if message.content == '!gn':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819111797686322/gn.png')
        await message.channel.send(embed=em)

    if message.content == '!gasp':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819116792971284/gasp.gif')
        await message.channel.send(embed=em)

    if message.content == '!belly':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819119028535316/fukbelly.gif')
        await message.channel.send(embed=em)

    if message.content == '!hangy':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819169372766219/hangy.png')
        await message.channel.send(embed=em)

    if message.content == '!happy':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819171436494852/happy.gif')
        await message.channel.send(embed=em)

    if message.content == '!horny':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819182668840990/horny.gif')
        await message.channel.send(embed=em)

    if message.content == '!hmm':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819183696576545/hmm.gif')
        await message.channel.send(embed=em)

    if message.content == '!goodjob':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819193968295957/goodjob.gif')
        await message.channel.send(embed=em)

    if message.content == '!good job':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819193968295957/goodjob.gif')
        await message.channel.send(embed=em)

    if message.content == '!hug':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819204181426187/hug.gif')
        await message.channel.send(embed=em)

    if message.content == '!hungry1':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819204718166036/hungry1.gif')
        await message.channel.send(embed=em)

    if message.content == '!hungry2':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819221130739742/hungry2.gif')
        await message.channel.send(embed=em)

    if message.content == '!laugh1':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819245482868738/laugh1.gif')
        await message.channel.send(embed=em)

    if message.content == '!laugh2':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819274121314306/laugh2.gif')
        await message.channel.send(embed=em)

    if message.content == '!comin thru':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819375615344651/nocchi.gif')
        await message.channel.send(embed=em)

    if message.content == '!point':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819376882024449/nice.gif')
        await message.channel.send(embed=em)

    if message.content == '!no':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819380493058058/nonono.gif')
        await message.channel.send(embed=em)

    if message.content == '!piss':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819408876175361/pee.gif')
        await message.channel.send(embed=em)

    if message.content == '!pikachu':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819467160092672/pikachu.gif')
        await message.channel.send(embed=em)

    if message.content == '!puke':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819467763941386/puke.gif')
        await message.channel.send(embed=em)

    if message.content == '!pervert':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819470888697858/pervert.gif')
        await message.channel.send(embed=em)

    if message.content == '!play':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819477784395777/play.gif')
        await message.channel.send(embed=em)

    if message.content == '!ricardo':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819633568972810/ricardo.gif')
        await message.channel.send(embed=em)

    if message.content == '!wake':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819648882507816/rise.gif')
        await message.channel.send(embed=em)

    if message.content == '!wakeup':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819648882507816/rise.gif')
        await message.channel.send(embed=em)
    
    if message.content == '!wake up':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819648882507816/rise.gif')
        await message.channel.send(embed=em)

    if message.content == '!sad':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819687998586900/sad.gif')
        await message.channel.send(embed=em)

    if message.content == '!shock':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819690586472467/shock.gif')
        await message.channel.send(embed=em)

    if message.content == '!shocked':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819690586472467/shock.gif')
        await message.channel.send(embed=em)

    if message.content == '!sexy':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819697599348737/sexy.gif')
        await message.channel.send(embed=em)

    if message.content == '!slap':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819698454855690/slap.gif')
        await message.channel.send(embed=em)

    if message.content == '!sleep':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819759398092820/sleepy.gif')
        await message.channel.send(embed=em)

    if message.content == '!sleepy':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819759398092820/sleepy.gif')
        await message.channel.send(embed=em)

    if message.content == '!nap':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819759398092820/sleepy.gif')
        await message.channel.send(embed=em)

    if message.content == '!bye':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819759398092820/sleepy.gif')
        await message.channel.send(embed=em)

    if message.content == '!sneeze':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819816365260841/sneeze.gif')
        await message.channel.send(embed=em)

    if message.content == '!spin':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819821063012374/spin.gif')
        await message.channel.send(embed=em)

    if message.content == '!snot':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819821914193921/snot.gif')
        await message.channel.send(embed=em)

    if message.content == '!sniff':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819825836130304/sniff.gif')
        await message.channel.send(embed=em)

    if message.content == '!strip':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819851647746072/strip.gif')
        await message.channel.send(embed=em)

    if message.content == '!stinky':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819880005566464/stinky.gif')
        await message.channel.send(embed=em)

    if message.content == '!wink':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819942165020689/suck.gif')
        await message.channel.send(embed=em)

    if message.content == '!ohdear':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819971080421396/uhh.gif')
        await message.channel.send(embed=em)

    if message.content == '!oh dear':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641819971080421396/uhh.gif')
        await message.channel.send(embed=em)

    if message.content == '!yeah':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641820001514422274/yeah.gif')
        await message.channel.send(embed=em)

    if message.content == '!yea':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641820001514422274/yeah.gif')
        await message.channel.send(embed=em)

    if message.content == '!ya':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641820001514422274/yeah.gif')
        await message.channel.send(embed=em)

    if message.content == '!yes':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641820001514422274/yeah.gif')
        await message.channel.send(embed=em)

    if message.content == '!suck':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641820286492213270/sucky.gif')
        await message.channel.send(embed=em)

    if message.content == '!punch':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641820499432833034/punch.gif')
        await message.channel.send(embed=em)

    if message.content == '!kiss3':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641825497860407326/Kechon_kiss.gif')
        await message.channel.send(embed=em)

    if message.content == '!shake':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641832953919438859/tumblr_lkg2miWevm1qb8q4h.gif')
        await message.channel.send(embed=em)

    if message.content == '!achan':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641833111847698483/3a07bb9218a6cd0944528f3446e0749d77772a506c4d235ad4360b1ee4bc3539.gif')
        await message.channel.send(embed=em)

    if message.content == '!a chan':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641833111847698483/3a07bb9218a6cd0944528f3446e0749d77772a506c4d235ad4360b1ee4bc3539.gif')
        await message.channel.send(embed=em)

    if message.content == '!yuka':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641833184644038666/WRiAx4B.gif')
        await message.channel.send(embed=em)

    if message.content == '!kashiyuka':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641833184644038666/WRiAx4B.gif')
        await message.channel.send(embed=em)

    if message.content == '!kashi':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641833184644038666/WRiAx4B.gif')
        await message.channel.send(embed=em)

    if message.content == '!smug':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641833245800923149/z0UYKa8.gif')
        await message.channel.send(embed=em)

    if message.content == '!tummy':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641833530594295828/look_at_her_go.gif')
        await message.channel.send(embed=em)

    if message.content == '!autism':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641833530594295828/look_at_her_go.gif')
        await message.channel.send(embed=em)

    if message.content == '!rock':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641833627805548554/nocchi_rocks.gif')
        await message.channel.send(embed=em)

    if message.content == '!suspicious':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/641833729165230090/400.gif')
        await message.channel.send(embed=em)
                            

    if message.content == '!sex':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640539027342360578/1437992512991.gif')
        await message.channel.send(embed=em)

    if message.content == '!jam':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640539502749941770/1557883318008.gif')
        await message.channel.send(embed=em)

    if message.content == '!wtf':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640539143637827584/eh.gif')
        await message.channel.send(embed=em)

    if message.content == '!moa':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640539196032811010/squish.gif')
        await message.channel.send(embed=em)

    if message.content == '!dontlook':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640539364127932437/04gk8.png')
        await message.channel.send(embed=em)

    if message.content == '!dont look':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640539364127932437/04gk8.png')
        await message.channel.send(embed=em)

    if message.content == '!yui':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/640375943659257878/640539443513524234/gcyui.gif')
        await message.channel.send(embed=em)
 
    if message.content.startswith('!hi'):
        await message.channel.send('hi <@%s> :-)'  %(message.author.id))
    if message.content.startswith('!hello'):
        await message.channel.send('hello <@%s> :-0'  %(message.author.id))
    if message.content.startswith('!ur cute'):
        await message.channel.send(":flushed: rly??")
    if message.content.startswith('!youre cute'):
        await message.channel.send(":flushed: rly??")
        
client.run('NjQwMzc2NTc0NjI5MTE3OTcy.Xb66Ew.ckaFekewcLHDfr8aGF0uo5n9OvI')
