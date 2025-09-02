# obsdatetime
A Python script that updates a text file with the current system time.
Can be used for real time watermarks (e.g.: fake security camera scene)
# Usage
Open the script. Note of where the script is stored.
Note: Any file that shares the filename of whatever file is named will have their contents purged because OBS reads the entire contents of a text file it's told to read from.
In other words, put the script in it's own folder, for your safety and my sanity (since I don't like going through GitHub Issues often.)
Use **Text (GDI+)**, set it up to **Read from File**, then link it to the file in the running directory of the script. Should be named "OBSTimeDate.txt"
# To-dos:
* Make sure the script runs every second.
  * (Mostly because in it's current state, it runs every time the routine of updating the text file is completed, and that's not exactly efficient.
* Allow user to change the name of the text file that writes to the time.
