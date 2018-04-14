# MUSIC DB  
This Python script converts the XML feed from Dr. Chuck Severance's iTunes Library (called Library.xml)
into an SQLite database.  

The script creates three tables, Artist, Album and Track, and runs
a join operation across three to create a view as follows:  

Track | Artist Name | Album Name | Length | Rating | Play Count |  
---| ---| ---| --- | ---- | --- |  
Another one bits the dust | Queen | Greatest Hits | 4:63 | 5 | 64 |  
  
The Library.xml file was provided by Dr. Chuck Severance through is book
Python For Everybody, and is publicly available. 

