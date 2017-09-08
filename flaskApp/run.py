from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '''
<!DOCTYPE html>
<html>
  <head>
    <title>BCIVr</title>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"/>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato"/>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>

    <script src="/socket.io/socket.io.js"></script>

    <link href="https://cdnjs.cloudflare.com/ajax/libs/rangeslider.js/2.3.1/rangeslider.css" rel="stylesheet" type="text/css"/>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>


    <style>
    body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
    .w3-bar,h1,button {font-family: "Montserrat", sans-serif}
    .fa-anchor,.fa-coffee {font-size:200px}
    </style>


  </head>

  <body>

    <header class="w3-container w3-red w3-center" style="padding:64px 16px">
      <h1 class="w3-margin w3-jumbo">BMEN 5411</h1>
      <h1 class="w3-margin w3-jumbo">Introduction to Neural Engineering</h1>

      <main id="lines"></main>
      <script>
      function getBCI(val){
        socket.emit('bciStream',{val})
      };
        var lines = document.querySelector('#lines');
        socket.on('brainwave',function(brainwave){
          var line = document.createElement('pre');
          line.innerHTML = 'Channel data: '+brainwave.channelData;
          lines.insertBefore(line,lines.firstChild);
        });
      </script>


    </header>

    <header class="w3-container w3-white w3-center">

      <div style="position:absolute;left:800px;top:500px;width: 300px;height: 200px;" >
        <input class="w3-button w3-black w3-large w3-margin-top" type="button" onclick="UserAction('status')"value="Get Home Status"/>
        <p id="energy_totalStatus">Total energy:</p>
        <p id="energy_miner1Status">Miner1</p>
        <p id="energy_miner2Status">Miner2</p>
        <p id="energy_solarStatus">Solar</p>
        <p id="hashrateStatus">Hashrate</p>
      </div>

      <div>


      <div style="position:absolute;left:850px;top:900px;">
        <h3>Lightbulbs</h3>
        <div>
          <text class="w3-black">Bookcase</text>
          <input type="range" min="-0" max="254" value="-10" id="Slider1">
          <output1></output1>
        </div>

        <div>
          <text class="w3-black">Computer</text>
          <input type="range" min="-0" max="254" value="-10" id="Slider2">
          <output2></output2>
        </div>
        <input class="w3-button w3-black w3-margin-top" type="button" onclick="UserAction('TP', '1')"value="Turn kitchen light on"/>
        <input class="w3-button w3-black w3-margin-top" type="button" onclick="UserAction('TP', '0')"value="Turn kitchen light off"/>
      </div>

    </header>
    <footer class="w3-container w3-red w3-bottom w3-center" style="padding:0px 0px 16px 0px">

      <div>
        <input class="w3-button w3-black w3-large w3-margin-top" type="button" onclick="Roku('poweron')"value="ROKU POWER ON"/>
        <input class="w3-button w3-black w3-large w3-margin-top" type="button" onclick="Roku('poweroff')"value="ROKU POWER OFF"/>
      </div>
</footer>

    <script>
    function Roku(input){
      socket.emit('TV',{input});
      };
    </script>

    <script>
      function UserAction(input, val){
        console.log(input);
        if(input=='status')
        {
          socket.emit('send message');
          socket.on('new message', function(data1,data2,data3, data4, data5){
          document.getElementById("energy_totalStatus").innerHTML = ("Current energy usage is: " + data1 + " Watts");
          document.getElementById("energy_miner1Status").innerHTML = ("Miner1 is using: " + data2 + " Watts");
          document.getElementById("energy_miner2Status").innerHTML = ("Miner2 is using: " + -1*data3 + " Watts");
          document.getElementById("energy_solarStatus").innerHTML = ("Currently generating: " + -1*data4 + " Watts");
          document.getElementById("hashrateStatus").innerHTML = ("Current hashrate is: " + data5.total_hashrate_calculated + " MH/s");
        });
      };
      if(input=='TP')
      {
        console.log({val});
        socket.emit('lightbulb',{val});
      }
      };
    </script>

    <script>
    $(function() {
        var $document = $(document);
        var selector = '[data-rangeslider]';
        var $element = $(selector);
        // For ie8 support
        var textContent = ('textContent' in document) ? 'textContent' : 'innerText';
        // Example functionality to demonstrate a value feedback
        function valueOutput(id, element) {
            var value = element.value;
            if(id=="Slider1"){
              var output1 = element.parentNode.getElementsByTagName('output1')[0] || element.parentNode.parentNode.getElementsByTagName('output1')[0];
              output1[textContent] = value;
              state = 1;
              socket.emit('lightbulb',{value, state});
            }
            else if (id=="Slider2") {
              var output2 = element.parentNode.getElementsByTagName('output2')[0] || element.parentNode.parentNode.getElementsByTagName('output2')[0];
              output2[textContent] = value;
              state = 2;
              socket.emit('lightbulb',{value, state});
            }
        }
        $document.on('input', 'input[type="range"], ' + selector, function(e) {
          console.log(e.target.id);
            valueOutput(e.target.id, e.target);
        });
    });
    </script>

  </body>
</html>
'''
app.run(host='0.0.0.0',port = 5030, debug=True)