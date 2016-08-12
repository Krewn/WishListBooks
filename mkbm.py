# coding: utf-8
import os
os.chdir("/home/kevin/books")
myFile = open("saved.pyDat","r")

content = myFile.read()

lines = [eval(k) for k in content.split("\n") if k != ""]

output = """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8"/>
		<meta name="viewport" content="width=device-width, user-scalable=yes, minimum-scale=1.0, maximum-scale=1.0">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
		<link href='https://fonts.googleapis.com/css?family=Arvo' rel='stylesheet' type='text/css'>
		<link rel="stylesheet" type="text/css" href="./mypage.css">
		<title>Kevin's Book Wishlist</title>
	</head>
	<body>	<!--<a href="https://www.metavision.com/" style="display: inline-block; position: absolute; opacity: 0.88;"><img src="https://s.adroll.com/a/7LS/UFO/7LSUFOLSEZFR3K7UCV4PST.jpg" width="160" height="600" border="0" alt="" style=" _width:158px; _height:598px; _overflow:hidden; border:1px solid #000000;margin:-1px;"></a>!-->
		<div class = "ClearShadeLeft">
			<div class="blue1" id = "infoDiv">
				<h1 id = "nameHeader">
					Books Marked
				</h1><br>
			</div><br>

			<div id = "langsAndLinks">
				<div class = "blue2" id = "pro">
					<h2 id = "Preferred Stack"> ... </h2><br>
					"""
lines.sort()
for k in lines:
	output +="\t\t\t\t\t\t\t<a href = "+ str(k[1])+"><font>"+ str(k[0])+"</font></a><br>\n"



output +="""<br>
				</div><br>
				<div class = "blue3">
					<div class="list-group">
						<a href="https://github.com/krewn" class="icon-link"><i class="fa fa-github fa-2x"></i></a>
						<a href="https://www.linkedin.com/in/kevin-nelson-0a499980" class="icon-link"><i class="fa fa-linkedin fa-2x"></i></a>
						<a href="https://www.facebook.com/Kevinb867" class="icon-link"><i class="fa fa-facebook fa-2x"></i></a>
						<a href="https://twitter.com/freelancephilos" class="icon-link"><i class="fa fa-twitter fa-2x"></i></a>
						<a href="https://krewn.github.io/Reprogramming" class="icon-link"><i class="fa fa-asterisk fa-2x"></i></a><br>
						<div class="white">
							<a href="https://krewn.github.io/bukeVote/" id="fl">Vute</a><a id = "fc">blog</a><a href="https://krewn.github.io/ApophysisOutPuts/" id ="fr">imgs</a>
							<a href="mailto:kpie314@gmail.com", id= "fc">kpie314@gmail.com</a><br>
							<font id = "fc">(802)-760-0677</font><br>
							<a href="https://krewn.github.io/KevinNelson.pdf">Resume</a>
							<a href="https://krewn.github.io/AgileContracts">Agile Contracts</a><br>
						</div>
					</div>
				</div>
			</div>
		</div><br>
		<script src="http://www.threejs.org/build/three.min.js"></script>
		<script src="http://www.threejs.org/examples/js/libs/stats.min.js"></script>
		<script src="http://www.threejs.org/examples/js/Detector.js"></script>
		<script src="PrettyGraphics.js"></script>
	</body>
</html>
"""
opFile = open("index.html","w")
opFile.write(output)
opFile.close()


