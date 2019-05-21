function move() {
    var elem = document.getElementById("myBar");   
    var width = 1;
    var id = setInterval(frame, 10);
    setTimeout(goback,1000)
    function frame() {
      if (width >= 100) {
        clearInterval(id);
      } else {
        width++; 
        elem.style.width = width + '%'; 
      }
    }
}

  function goback(){
    $(location).attr('href', 'index.html')

  }

  function addBookPage()
  {
    $(location).attr('href', 'new.html')

  }
  