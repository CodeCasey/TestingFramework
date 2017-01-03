
# SyntaxError myList script
# Objective: write a script that lists the top-level directory contents of the containing dir.
# in a .html file displayed in a browser. 

#!/bin/sh

echo "<br><font color ="red">SyntaxErr myList.sh Script Results: </font> </br>" > myList_SyntaxErr.html

# list directory content in .html file

for i in *
 do 
   echo "<br>$i<br/>" >> myList_SyntaxErr.html
done


# grant user permissions... open user default browser to open .html file

chmod 755 myList_SyntaxErr.html
xdg-open myList_SyntaxErr.html
