function startTime() {
    var today = new Date();
    var now = today.toLocaleString([],
              { hour: '2-digit', minute: '2-digit', second: '2-digit' });

    document.getElementById('time').innerHTML = now;
    var t = setTimeout(startTime, 500);
}

function colorGenerator() {
  var colors = ['#42CAFD', '#8B80F9', '#2DE1C2', '#247BA0', '#DD403A'];
  var choice = Math.floor(Math.random() * 5);
  var color = colors[choice];
  return color;
}

function assignColor() {
  var containers = document.getElementsByClassName('project-container');
  for(var i = 0; i < containers.length; i++) {
    containers[i].style.backgroundColor = colorGenerator();
  }
}
