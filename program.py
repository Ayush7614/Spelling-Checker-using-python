from textblob import TextBlob 
a = "mobil"  
b = TextBlob(a) 
print("corrected text: ", b.correct())
