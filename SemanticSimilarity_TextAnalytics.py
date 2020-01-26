import urllib.request
import json

li= ["good morning" , "how are you doing ?", "the weather is awesome today","samsung","good afternoon", "baseball is played in the USA","there is a thunderstorm", "are you doing good ?","The polar regions are melting","apple","nokia","cricket is a fun game","the climate change is a problem"]

for txt1 in li:
    for txt2 in li:
        
        with urllib.request.urlopen("https://api.dandelion.eu/datatxt/sim/v1/?text1="+urllib.parse.quote(txt1)+"&text2="+urllib.parse.quote(txt2)+"&lang=en&token=aa9762e4dd6c45208a8d37cad06dc62a") as response:
                resp=response.read()
                sim=json.loads(resp)["similarity"]*100
                if sim!=0.0 and sim !=100.0 and sim>30:
                    print('Text1 :',txt1,'\nText2 :',txt2)
                    print("Semantic Similarity :",str(sim)+"%")
