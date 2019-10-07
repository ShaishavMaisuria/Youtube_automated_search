
#-------------------------------------------------------
# write the file
def NewFileCreate(bsoup):

    f = open("YoutubeData.html", "w+")
    f.write(bsoup)
    f.close()
#code

#-------------------------------------------------------
# append the file
def AppendFile(bsoup):
    f = open("YoutubeData.txt", "a+")
    f.write(bsoup)
    f.close()


# code

# -------------------------------------------------------

# Read the file doesnot work with
def ReadFile():
    with open("YoutubeData.txt", "r",encoding="utf-8") as f:
        if(f.mode=='r'):
         data=f.read()
         print(data) #you can indent outside the if statement
    f.close()


# code

# -------------------------------------------------------
existingFile=open("YotubeData.html","w+",encoding="utf-8")
with open("YoutubeData.txt", "r",encoding="utf-8") as f:
        if(f.mode=='r'):
         data=f.read()
         existingFile.write(data)
        print(data)
        f.close()