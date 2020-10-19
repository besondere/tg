import os
await reply.download_media("tgs.tgs")
os.system("lottie_convert.py tgs.tgs json.json")
json = open("json.json","r")
jsn = json.read()
json.close()
jsn = jsn.replace('[1]','[10]').replace('[2]','[20]').replace('[3]','[30]').replace('[4]','[40]').replace('[5]','[50]')

open("json.json","w").write(jsn)
os.system("lottie_convert.py json.json tgs.tgs")
await reply.reply(file="tgs.tgs")
os.remove("json.json")
os.remove("tgs.tgs")
await message.delete()