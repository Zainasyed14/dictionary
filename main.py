Books = {
    "The Cruel Prince" : "Holly Black" ,
    "Once Upon  A Broken Heart" : "Stephanie Gerber",
    "A Good Girls Guide To Murder" : "Holly Jackson",
    "Powerless" : "Lauren Roberts",
    "Fourth Wing" : "Rebecca Yarros", 
}

# print(Books)

Books["The Good Doctor"] = "Ana Huang"
print(Books)
# print("the legnth of the dictionary is", len(Books))

# print(Books)
# Books.clear()
# print(Books)
Books.pop("Fourth Wing")
print(Books)
print(Books.get("AuthorName", "Key doesnt exist"))
for i in Books:
    print("Key : " , i , "Value :" , Books.get(i))