with open("words_list.txt", "r") as file:
	words = file.read().splitlines()

print("start typing in your letters maybe type 1/2/3 letters and hit enter")
uword=input("Enter the letter(s): ")

def match(uword,word):
	ref=0
	if len(uword)>len(word):
		return
	while ref<=len(uword)-1:
		if uword[ref]==word[ref]:
			ref+=1
		else:
			break
	if ref==len(uword):
		return(word)

def get_suggestions(uword):
	count=0
	for word in words:
		if match(uword,word):
			print(word)
			count+=1
			if count==5:
				break #This is temporary break so that your system isn't bimbed with 500+ suggestions.
	print("Total",count,"words matched")

get_suggestions(uword)
