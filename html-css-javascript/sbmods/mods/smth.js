/*let conwayPhase = 0;

function isInBounds(x, y) {
    return x >= 0 && x < pixelMap.length && y >= 0 && y < pixelMap[0].length;
}*/

elements.mint = {
	color: "#aaffaa",
	behavior: behaviors.POWDER,
	category: "misc",
	state: "solid",
	tempHigh: 300,
	stateHigh: "dust",
	reactions: {
		"water": { elem1: "foam", elem2: "water" },
        "soda": { elem1: "explosion", elem2: "explosion" },
	}
}

elements.linerx = {
	color: "#ff00ff",
	behavior: behaviors.POWDER,
	category: "misc",
	state: "solid",
	tick: function(pixel) {
        tryMove(pixel,pixel.x,pixel.y-1);
	}
}

elements.patternpowder = {
	color: "#ffff00",
	behavior: behaviors.POWDER,
	category: "misc",
	state: "solid",
	tick: function(pixel) {
        tryMove(pixel,pixel.x-2,pixel.y-1);
        tryMove(pixel,pixel.x+2,pixel.y);
	}
}

/*elements.conway = {
    color: "#00ff00",
    category: "misc",
    state: "solid",
    tick: function(pixel) {
        if (!conwayPhase) {
            let nbrs = [
                pixelMap[pixel.x+1]?.[pixel.y+1],
                pixelMap[pixel.x+1]?.[pixel.y],
                pixelMap[pixel.x+1]?.[pixel.y-1],
                pixelMap[pixel.x]?.[pixel.y+1],
                pixelMap[pixel.x]?.[pixel.y-1],
                pixelMap[pixel.x-1]?.[pixel.y+1],
                pixelMap[pixel.x-1]?.[pixel.y],
                pixelMap[pixel.x-1]?.[pixel.y-1],
            ];
            let liveCells = 0;
            for (let nbr of nbrs) {
                if (nbr && nbr.element === "conway") {
                    liveCells++;
                }
            }
            pixel.newState = (liveCells == 2 || liveCells == 3) ? 1 : 0;
        } else {
            if (!pixel.newState) {
                if (isInBounds(pixel.x, pixel.y)) {
                    changePixel(pixel, "conwayDead");
                }
            }
        }
    },
    onChange: function(pixel, newElement) {
        // do nothing
    },
}

elements.conwayDead = {
    color: "#003300",
    category: "misc",
	state: "solid",
	density: 0,
	hardness: 0,
	behavior: behaviors.STILL,
    tick: function(pixel) {
        if (!conwayPhase) {
            let nbrs = [
                pixelMap[pixel.x+1]?.[pixel.y+1],
                pixelMap[pixel.x+1]?.[pixel.y],
                pixelMap[pixel.x+1]?.[pixel.y-1],
                pixelMap[pixel.x]?.[pixel.y+1],
                pixelMap[pixel.x]?.[pixel.y-1],
                pixelMap[pixel.x-1]?.[pixel.y+1],
                pixelMap[pixel.x-1]?.[pixel.y],
                pixelMap[pixel.x-1]?.[pixel.y-1],
            ];
            let liveCells = 0;
            for (let nbr of nbrs) {
                if (nbr && nbr.element === "conway") {
                    liveCells++;
                }
            }
            pixel.beAlive = (liveCells === 3);
        } else {
            if (pixel.beAlive) {
                if (isInBounds(pixel.x, pixel.y)) {
                    changePixel(pixel, "conway");
                }
            }
        }
    },
    onChange: function(pixel, newElement) {
        // do nothing
    },
}

elements.conwayManager = {
    color: "#ff00ff",
    category: "misc",
    state: "solid",
    tick: function(pixel) {
        conwayPhase = 1 - conwayPhase;  // toggle 0/1 each tick
    }
}*/

elements.bore = {
    color: "#aaaaaa",
    behavior: [
        ["XX", "XX", "XX"],
        ["DL", "XX", "DL"],
        ["DL", "DL AND M1", "DL"]
    ],
    category: "misc",
    state: "solid",
}

elements.irratic = {
    color: "#ffaa00",
    behavior: [
        ["M1", "M1", "M1"],
        ["M1", "XX", "M1"],
        ["M1", "M1", "M1"]
    ],
    category: "misc",
    state: "solid",
    reactions: {
        "linerx": {elem1: "nuke", elem2: "nuke"}
    }
}
