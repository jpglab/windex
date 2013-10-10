function countdown(){
  var now = moment();
  var wedding = moment([2014, 8, 6]);
  var diff = wedding.diff(now);
  var M = moment.duration(diff).months();
  var d = moment.duration(diff).days();
  var h = moment.duration(diff).hours();
  var m = moment.duration(diff).minutes();
  var s = moment.duration(diff).seconds();
  var cdiv = document.getElementById("countdown");
  cdiv.innerHTML = "<table>"
                    +"<tbody>"
                    +"<tr>"
                    +"<td class=\"big\">"+M+"</td>"
                    +"<td class=\"big\">"+d+"</td>"
                    +"<td class=\"big\">"+h+"</td>"
                    +"<td class=\"big\">"+m+"</td>"
                    +"<td class=\"big\">"+s+"</td>"
                    +"</tr>"
                    +"<tr>"
                    +"<td>Months</td>"
                    +"<td>Days</td>"
                    +"<td>Hours</td>"
                    +"<td>Minutes</td>"
                    +"<td>Seconds</td>"
                    +"</tr>"
                    +"</tbody>"
                    +"</table>";
} 
var i = setInterval(countdown, 1000);
