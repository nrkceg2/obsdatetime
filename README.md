# obsdatetime
A Python script that updates a text file with the current system time.<br>
Can be used for real time watermarks (e.g.: fake security camera scene)<br>
This is the first time I've ever used Python for something, please don't smite me.
# Usage
Open the script. Note of where the script is stored.<br>
Note: Any file that shares the filename of whatever file is named will have their contents purged because OBS reads the entire contents of a text file it's told to read from.<br>
In other words, put the script in it's own folder, for your safety and my sanity (since I don't like going through GitHub Issues often.)<br>
Use **Text (GDI+)**, set it up to **Read from File**, then link it to the file in the running directory of the script. Should be named "OBSTimeDate.txt" or whatever you decided to name it.
# To-dos
* Create more to-dos.
* Upload latest pre-release.
* Easy to follow tutorial.
# Requirements
* Literally just Python
* A clock, probably.
* OBS (Or something similar)
* A computer
* Python 3.x (originally made on 3.13.2)
# Screenshots:
<img width=350px src=screenshots/screenshot-0.png>
# For contributors:
* Add yourself in the script!<br>
`print("name (GitHub Profile link or website)")`
* In comments:<br>
`# whatever you wanna say - [shortened name] day-Short Month-YYYY HH:mm (24hr time)`
* In Readme:<br>
`* <a href="https://github.com/profilename">Name</a> - List of your additions, keep it succinct, nothing too long, please.`
# Contributors
* <a href="https://github.com/nrkceg2">nrkceg2</a> - Initial release, original concept, script creation, testing.
* <a href="https://github.com/billysb">BillySB</a> - Optimizations, various suggestions for efficiency, slight re-writes to existing work.
