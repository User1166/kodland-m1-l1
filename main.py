meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "AFK": "klavyeden uzakta",
            "NPC": "bot"
            }
            

for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        # Kelime eşleşiyorsa ne yapmalıyız?
        print(meme_dict[word])
    else:
        # Kelime eşleşmiyorsa ne yapmalıyız?
        print("bilmiyoruz")
