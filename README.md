# obsdatetime
A Python script that updates a text file with the current system time.
Can be used for real time watermarks (e.g.: fake security camera scene)
# Usage
Open the script. Note of where the script is stored.
Use **Text (GDI+)**, set it up to **Read from File**, then link it to the file in the running directory of the script.
# To-dos:
* Make sure the script runs every second.
  * (Mostly because in it's current state, it runs every time the routine of updating the text file is completed, and that's not exactly efficient.
