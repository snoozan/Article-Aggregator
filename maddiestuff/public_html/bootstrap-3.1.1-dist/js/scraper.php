<?
	Header("content-type: application/x-javascript");
	$tempJsonArray = row_to_json(row("http://spectrum.ieee.org/aerospace/satellites/japans-plan-for-centimeterresolution-gps", "Japan’s Plan for Centimeter-Resolution GPS", "A stranger to Tokyo could easily get lost in its urban canyons. And GPS navigation, stymied by low resolution and a blocked view of the sky, might not be much help."));	
	
	echo "document.write(\"The Answer is: <b>" . $tempJsonArray . "</b>\")";
		
?>