$( window ).load(function() {
  var img = ["header.jpg", "header2.jpg", "header3.jpg"];
  var r = Math.floor(Math.random()*3);
  $( "#header" ).css("background-image", "url(/static/img/" + img[r] + ")");
});
