function startTime() {
    var today = new Date();
    var now = today.toLocaleString([],
              { hour: '2-digit', minute: '2-digit', second: '2-digit' });

    document.getElementById('time').innerHTML = now;
    var t = setTimeout(startTime, 500);
}

// TODO: Create handler to start time clock on clock in in the success action
function clock_in_start() {
  $.ajax({
    url: window.location.href + "/clock-in",
    type: 'GET',
    dataType: 'json',
    success: function(data){
      console.log(data.clock_in);
      console.log(data.in_work);
    }
  })
}

// TODO: create handler to process elepsed time and send back to db to process
//       the entire used time and readjust the project estimate.
function clock_out_start() {
  $.ajax({
    url: window.location.href + '/clock-out',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      console.log(data.clock_out);
      console.log(data.in_work);
    }
  })
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

function onPageLoad() {
  // Create a function to call the loadProjectsTab() function so that the
  // function executes after a page load.
}

function loadProjectsTab(){

  alert(location);
  document.getElementById('overview').classList.remove("active");
  document.getElementById('overview-tab').classList.remove(" ctive");
  document.getElementById('projects').classList.add("active");
  document.getElementById('projects-tab').classList.add("active");
  // alert("'clicked'");
}
