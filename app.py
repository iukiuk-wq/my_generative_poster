import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Unique Tree",
    page_icon="🌳",
    layout="wide"
)

st.title("UNIQUE TREE")
st.write("Web-based Generative Poster • Arts & Advanced Big Data")

html_code = r"""
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">

<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.js"></script>

<style>

body {
    margin: 0;
    padding: 20px;
    background: #f3f0e8;
    font-family: Arial, sans-serif;
}

.container {
    display: flex;
    gap: 30px;
    align-items: flex-start;
}

.controls {
    width: 230px;
    background: #ffffff;
    padding: 22px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.12);
}

.controls h2 {
    margin-top: 0;
    font-size: 20px;
}

.control-group {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 7px;
    font-size: 14px;
    font-weight: bold;
}

input[type="range"] {
    width: 100%;
}

select {
    width: 100%;
    padding: 7px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.value {
    font-size: 13px;
    color: #666;
    margin-top: 3px;
}

button {
    width: 100%;
    padding: 11px;
    margin-top: 8px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
}

#generateButton {
    background: #30382f;
    color: white;
}

#randomButton {
    background: #dedbd0;
    color: #333;
}

.poster-container {
    background: white;
    padding: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.18);
}

</style>
</head>


<body>

<div class="container">

<div class="controls">

<h2>Tree Controls</h2>


<div class="control-group">

<label>Growth</label>

<input
type="range"
id="growth"
min="3"
max="8"
value="6"
>

<div class="value">
<span id="growthValue">6</span>
</div>

</div>


<div class="control-group">

<label>Branches</label>

<input
type="range"
id="branches"
min="1"
max="4"
value="2"
>

<div class="value">
<span id="branchesValue">2</span>
</div>

</div>


<div class="control-group">

<label>Wobble</label>

<input
type="range"
id="wobble"
min="0"
max="50"
value="18"
>

<div class="value">
<span id="wobbleValue">18</span>
</div>

</div>


<div class="control-group">

<label>Leaves</label>

<input
type="range"
id="leaves"
min="0"
max="100"
value="60"
>

<div class="value">
<span id="leavesValue">60</span>
</div>

</div>


<div class="control-group">

<label>Season</label>

<select id="season">

<option value="spring">Spring</option>
<option value="summer">Summer</option>
<option value="autumn" selected>Autumn</option>
<option value="winter">Winter</option>

</select>

</div>


<div class="control-group">

<label>Seed</label>

<input
type="range"
id="seed"
min="1"
max="9999"
value="2026"
>

<div class="value">
<span id="seedValue">2026</span>
</div>

</div>


<button id="generateButton">
GENERATE TREE
</button>

<button id="randomButton">
RANDOM TREE
</button>

</div>


<div class="poster-container">

<div id="canvas-container"></div>

</div>

</div>


<script>

let growth = 6;
let branches = 2;
let wobble = 18;
let leafDensity = 60;
let season = "autumn";
let seed = 2026;


/* -------------------------
   P5 SETUP
------------------------- */

function setup() {

    let canvas = createCanvas(600, 800);

    canvas.parent("canvas-container");

    noLoop();

    updateValues();

    drawTreePoster();
}


/* -------------------------
   DRAW
------------------------- */

function draw() {

    drawTreePoster();

}


/* -------------------------
   MAIN POSTER
------------------------- */

function drawTreePoster() {

    randomSeed(seed);
    noiseSeed(seed);

    background(246, 243, 235);


    /*
       subtle background
    */

    drawBackground();


    /*
       title
    */

    fill(35);
    noStroke();

    textFont("Arial");
    textStyle(BOLD);
    textSize(30);
    textAlign(LEFT, TOP);

    text(
        "UNIQUE TREE",
        40,
        35
    );


    textStyle(NORMAL);
    textSize(14);

    fill(90);

    text(
        "ONE SEED / MANY FORMS",
        40,
        75
    );


    /*
       ground
    */

    drawGround();


    /*
       tree
    */

    push();

    translate(
        width / 2,
        height - 95
    );

    drawBranch(
        0,
        0,
        -HALF_PI,
        145,
        growth
    );

    pop();


    /*
       bottom information
    */

    stroke(70, 70, 70, 100);
    strokeWeight(0.5);

    line(
        40,
        height - 50,
        width - 40,
        height - 50
    );

    noStroke();

    fill(80);

    textSize(12);
    textAlign(LEFT, TOP);

    text(
        "GENERATIVE BOTANICAL SYSTEM",
        40,
        height - 38
    );

    textAlign(RIGHT, TOP);

    text(
        "SEED " + seed,
        width - 40,
        height - 38
    );

}


/* -------------------------
   BACKGROUND
------------------------- */

function drawBackground() {

    for (
        let y = 0;
        y < height;
        y += 4
    ) {

        let shade =
            map(
                y,
                0,
                height,
                250,
                238
            );

        stroke(
            shade,
            shade - 2,
            shade - 8
        );

        line(
            0,
            y,
            width,
            y
        );
    }

}


/* -------------------------
   GROUND
------------------------- */

function drawGround() {

    noStroke();

    fill(210, 204, 188, 100);

    ellipse(
        width / 2,
        height - 88,
        380,
        35
    );

}


/* -------------------------
   BRANCH SYSTEM
------------------------- */

function drawBranch(
    x,
    y,
    angle,
    length,
    level
) {

    if (level <= 0) {

        createLeaves(
            x,
            y
        );

        return;
    }


    /*
       natural bending
    */

    let bend =
        random(
            -wobble,
            wobble
        );

    let newAngle =
        angle +
        radians(bend);


    let endX =
        x +
        cos(newAngle) *
        length;

    let endY =
        y +
        sin(newAngle) *
        length;


    /*
       branch thickness
    */

    let thickness =
        map(
            level,
            1,
            growth,
            1.2,
            15
        );

    stroke(
        65,
        52,
        42,
        235
    );

    strokeWeight(thickness);

    line(
        x,
        y,
        endX,
        endY
    );


    /*
       small natural bend
    */

    let midX =
        lerp(
            x,
            endX,
            0.5
        );

    let midY =
        lerp(
            y,
            endY,
            0.5
        );


    /*
       branching
    */

    for (
        let i = 0;
        i < branches;
        i++
    ) {

        let direction;

        if (branches === 1) {

            direction =
                random(
                    -0.45,
                    0.45
                );

        } else {

            direction =
                map(
                    i,
                    0,
                    branches - 1,
                    -0.65,
                    0.65
                );

            direction +=
                random(
                    -0.25,
                    0.25
                );
        }


        let nextAngle =
            newAngle +
            direction;


        let nextLength =
            length *
            random(
                0.62,
                0.78
            );


        drawBranch(
            endX,
            endY,
            nextAngle,
            nextLength,
            level - 1
        );

    }


    /*
       occasional small branch
    */

    if (
        random(1) <
        0.35
    ) {

        drawBranch(
            midX,
            midY,
            newAngle +
            random(
                -1.0,
                1.0
            ),
            length * 0.35,
            level - 2
        );

    }

}


/* -------------------------
   LEAVES
------------------------- */

function createLeaves(
    x,
    y
) {

    let amount =
        floor(
            leafDensity / 15
        );


    if (season === "winter") {

        amount = 0;

    }


    for (
        let i = 0;
        i < amount;
        i++
    ) {

        let offsetX =
            random(
                -22,
                22
            );

        let offsetY =
            random(
                -22,
                22
            );


        let leafX =
            x + offsetX;

        let leafY =
            y + offsetY;


        drawLeaf(
            leafX,
            leafY
        );

    }

}


/* -------------------------
   SINGLE LEAF
------------------------- */

function drawLeaf(
    x,
    y
) {

    let palette =
        getLeafPalette();


    let selected =
        random(palette);


    noStroke();

    fill(
        selected[0],
        selected[1],
        selected[2],
        selected[3]
    );


    let size =
        random(
            6,
            14
        );


    push();

    translate(
        x,
        y
    );

    rotate(
        random(
            TWO_PI
        )
    );


    ellipse(
        0,
        0,
        size,
        size * 1.7
    );

    pop();

}


/* -------------------------
   SEASON COLORS
------------------------- */

function getLeafPalette() {

    if (
        season === "spring"
    ) {

        return [

            [125, 170, 95, 190],
            [165, 195, 105, 190],
            [195, 210, 125, 180],
            [100, 150, 90, 180]

        ];

    }


    if (
        season === "summer"
    ) {

        return [

            [45, 105, 65, 200],
            [70, 130, 75, 200],
            [90, 145, 80, 190],
            [35, 90, 55, 190]

        ];

    }


    if (
        season === "autumn"
    ) {

        return [

            [175, 75, 45, 200],
            [210, 120, 45, 200],
            [190, 145, 55, 190],
            [145, 65, 40, 180]

        ];

    }


    return [

        [220, 220, 210, 180],
        [190, 200, 195, 180],
        [235, 235, 225, 170]

    ];

}


/* -------------------------
   UPDATE CONTROLS
------------------------- */

function updateValues() {

    growth =
        Number(
            document.getElementById(
                "growth"
            ).value
        );


    branches =
        Number(
            document.getElementById(
                "branches"
            ).value
        );


    wobble =
        Number(
            document.getElementById(
                "wobble"
            ).value
        );


    leafDensity =
        Number(
            document.getElementById(
                "leaves"
            ).value
        );


    season =
        document.getElementById(
            "season"
        ).value;


    seed =
        Number(
            document.getElementById(
                "seed"
            ).value
        );


    document.getElementById(
        "growthValue"
    ).innerText =
        growth;


    document.getElementById(
        "branchesValue"
    ).innerText =
        branches;


    document.getElementById(
        "wobbleValue"
    ).innerText =
        wobble;


    document.getElementById(
        "leavesValue"
    ).innerText =
        leafDensity;


    document.getElementById(
        "seedValue"
    ).innerText =
        seed;

}


/* -------------------------
   GENERATE BUTTON
------------------------- */

document
.getElementById(
    "generateButton"
)
.addEventListener(
    "click",
    function() {

        updateValues();

        redraw();

    }
);


/* -------------------------
   RANDOM TREE
------------------------- */

document
.getElementById(
    "randomButton"
)
.addEventListener(
    "click",
    function() {

        document.getElementById(
            "growth"
        ).value =
            floor(
                random(
                    4,
                    9
                )
            );


        document.getElementById(
            "branches"
        ).value =
            floor(
                random(
                    1,
                    5
                )
            );


        document.getElementById(
            "wobble"
        ).value =
            floor(
                random(
                    5,
                    45
                )
            );


        document.getElementById(
            "leaves"
        ).value =
            floor(
                random(
                    20,
                    101
                )
            );


        document.getElementById(
            "seed"
        ).value =
            floor(
                random(
                    1,
                    10000
                )
            );


        let seasons = [
            "spring",
            "summer",
            "autumn",
            "winter"
        ];


        document.getElementById(
            "season"
        ).value =
            random(
                seasons
            );


        updateValues();

        redraw();

    }
);


/* -------------------------
   LIVE VALUE DISPLAY
------------------------- */

document
.getElementById(
    "growth"
)
.addEventListener(
    "input",
    updateValues
);


document
.getElementById(
    "branches"
)
.addEventListener(
    "input",
    updateValues
);


document
.getElementById(
    "wobble"
)
.addEventListener(
    "input",
    updateValues
);


document
.getElementById(
    "leaves"
)
.addEventListener(
    "input",
    updateValues
);


document
.getElementById(
    "seed"
)
.addEventListener(
    "input",
    updateValues
);


document
.getElementById(
    "season"
)
.addEventListener(
    "change",
    updateValues
);

</script>

</body>
</html>
"""


components.html(
    html_code,
    height=900,
    scrolling=True
)
