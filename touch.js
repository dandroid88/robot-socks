$( document ).ready(function() {

    // Register button listeners
    $("#keyboard").click( function() {
        connection.send("inputtext." + prompt(""));
    });

    $(".button").mousedown( function(e) {
        connection.send("m." + e.target.id);
    });

    $(document).mouseup(function() {
        connection.send("m.stop");
    });

    $(document).keydown(function(e) {
        if (e.keyCode == 37) {
            connection.send("m.spin_left");
            return false;
        } else if (e.keyCode == 38) {
            connection.send("m.forward");
            return false;
        } else if (e.keyCode == 39) {
            connection.send("m.spin_right");
            return false;
        } else if (e.keyCode == 40) {
            connection.send("m.backword");
            return false;
        }
    });

    $(document).keyup(function(e) {
        connection.send("m.stop");
    });


    // Establish websocket connection and register error messages
    var connection;
    try {
        connection = new WebSocket("ws://" + window.location.hostname + ":8000/");
    } catch (e) {
        connection = new WebSocket("ws://localhost:8000/");
    }

    connection.onerror = function(error) {
        alert("Make sure the websocket server is running.");
    };

    connection.onclose = function() {
        alert("Socket is now closed.");
    };

    // Helper functions
    function init() {
        can = document.getElementById("touchpad");
        canvasWidth = document.getElementById('touchpad').offsetWidth;
        canvasHeight = document.getElementById('touchpad').offsetHeight;
        centerX = canvasWidth / 2;
        centerY = canvasHeight / 2;

        ctx = can.getContext("2d");
        ctx.translate(0.5, 0.5);
        ctx.beginPath();
        ctx.arc(centerX, centerY, 4, 0, 2*Math.PI, false);
        ctx.fillStyle = 'green';
        ctx.fill();
        ctx.lineWidth = 1;
        ctx.strokeStyle = '#000000';
        ctx.stroke();

        can.addEventListener("mouseup", mouseUp, false);
        can.addEventListener("mousedown", mouseDown, false);
        can.addEventListener("mousemove", mouseXY, false);
        can.addEventListener("touchstart", touchDown, false);
        can.addEventListener("touchmove", touchXY, true);
        can.addEventListener("touchend", touchUp, false);
    }

    function touchUp() {
        mouseIsDown = 0;
        // no touch to track, so just show state
        connection.send("t.Up");
    }

    function touchDown() {
        mouseIsDown = 1;
        connection.send("t.Down");
        touchXY();
    }

    function touchXY(e) {
        if (!e)
            var e = event;
        e.preventDefault();
        canX = e.targetTouches[0].pageX - can.offsetLeft;
        canY = e.targetTouches[0].pageY - can.offsetTop;
        connection.send("m." + canX + " " + canY);
    }

    function mouseUp() {
        mouseIsDown = 0;
        connection.send("m.Up");
        mouseXY();
    }

    function mouseDown() {
        mouseIsDown = 1;
        connection.send("m.Down");
        mouseXY();
    }

    function mouseXY(e) {
        if (!e)
            var e = event;
        canX = e.pageX - can.offsetLeft;
        canY = e.pageY - can.offsetTop;
        if (mouseIsDown) {
            connection.send("m." + ((canX - centerX) / centerX) + " " + ((canY - centerY) / (-1 * centerY)));
        }
    }

    var can, ctx, canX, canY, canvasWidth, canvasHeight, centerX, centerY ,mouseIsDown = 0;
    init();

});
