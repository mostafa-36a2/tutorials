times = document.getElementsByClassName("ytd-thumbnail-overlay-time-status-renderer");
minutes = 0;
seconds = 0;
for(var i=1;i<times.length;i+=2){
	video_time = times[i].innerText;
	mintes_seconds_array = video_time.split(':'); 
	minutes += parseInt(mintes_seconds_array[0]);
	seconds += parseInt(mintes_seconds_array[1]);
}

 
minutes += Math.floor(seconds/60);
houres = Math.floor(minutes/60);
minutes = minutes % 60;
seconds = seconds%60;
result = [houres,minutes,seconds].join(":")
alert("The total time for this playlist is: "+result)
