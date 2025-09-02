from datetime import datetime
import time
# Time it took to complete this script:
# Start date: Fri, 26 Aug 2025 [unknown time, I think first period so about 07:50]
# Didn't work on this at all over the weekend LOL.
# End date: Tue, 2 Sept 2025 09:13
print("Put this somewhere you can easily get to, the file this thing makes gets written into the running directory.")
print("I'm saying this for both your sake, my sanity, and so I don't get 8 thousand Issues on my GitHub.")
print("Signed, Nrkceg2. Script starts in about 5 seconds.")
time.sleep(5)
# print("P.S.: My name comes from a leaked Valve game. I can't remember which one, but BillySB might.")
# In hindsight, I would've named these "MakesMeWannaDie" & "MakesMeWannaDieEvenMore",
# but for the sake of code readability, I'm not doing that.
# Plus, I'm on my school laptop. I'm already trying not to get myself killed for doing something
# slightly wrong on these. I'm afraid to be my usual, brutally honest self when writing even the
# slightly snarkiest of code comments on here. - nrk 2-Sept-2025 09:12
fulldt = datetime.now()
# I removed d and t because they very clearly aren't needed. Will change ft accordingly.
ft = fulldt.strftime("%H:%M:%S \n%d %m %Y ") # format is HH:mm <line break> DD mmm YYYY

# Because I need a file name for the thing I shouldn't delete.    
# Should I make this user-defined? Yes.
# Will I? Hell no, too much work.
file = "OBSTimeDate.txt"
print("File is named the following:")
print(file)
print("Please note of this file's name and location for later usage.")

# the routine that does all of this bull.
print("Routine started! Press Ctrl+C to end the script safely. Or just exit the terminal, or whatever you run this in.")
while True:
    fulldt = datetime.now()
    ft = fulldt.strftime("%H:%M:%S \n%d %m %Y ")
    completiontime = fulldt.strftime("%H:%M:%S on %d-%m-%Y")
    with open(file, 'r+') as filemod:          
            filemod.seek(0)
            filemod.truncate()
            filemod.write(ft)
    print("Lap success! Completed at ", completiontime)