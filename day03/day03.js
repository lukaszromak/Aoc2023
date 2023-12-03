const reader = require("fs");

const day03 = () => {
    reader.readFile("input.txt", (err, data) => {
        // prevent index out of bounds
        const engineSchema = new String(data).split("\r\n").map((x) => "." + x + ".");
        engineSchema.unshift(".".repeat(engineSchema[0].length));
        engineSchema.push(".".repeat(engineSchema[0].length));

        let number = "";
        let count = 0;
        let gears = {};

        for(let i = 1; i < engineSchema.length - 1; i++){
            for(let j = 1; j < engineSchema[i].length; j++){
                if("1234567890".includes(engineSchema[i][j])){
                    number += engineSchema[i][j];
                }
                if((number != "" && !"0123456789".includes(engineSchema[i][j]))){
                    topSlice = engineSchema[i - 1].slice(j - number.length - 1, j + 1);
                    bottomSlice = engineSchema[i + 1].slice(j - number.length - 1, j + 1);
                    left = engineSchema[i][j - number.length - 1];
                    right = engineSchema[i][j];

                    for(let k = 0; k < topSlice.length; k++){
                        if(topSlice[k] == "*"){
                            if(!gears.hasOwnProperty((i - 1).toString() + (j - number.length - 1 + k).toString())){
                                gears[(i - 1).toString() + (j - number.length - 1 + k).toString()] = new Array(number);
                            } else {
                                gears[(i - 1).toString() + (j - number.length - 1 + k).toString()].push(number);
                            }
                        }
                    }

                    for(let k = 0; k < bottomSlice.length; k++){
                        if(bottomSlice[k] == "*"){
                            if(!gears.hasOwnProperty((i + 1).toString() + (j - number.length - 1 + k).toString())){
                                gears[(i + 1).toString() + (j - number.length - 1 + k).toString()] = new Array(number);
                            } else {
                                gears[(i + 1).toString() + (j - number.length - 1 + k).toString()].push(number);
                            }
                        }
                    }

                    if(left == "*"){
                        if(!gears.hasOwnProperty(i.toString() + (j - number.length - 1).toString())){
                            gears[i.toString() + (j - number.length - 1).toString()] = new Array(number);
                        } else {
                            gears[i.toString() + (j - number.length - 1).toString()].push(number);
                        }
                    }

                    if(right == "*"){
                        if(!gears.hasOwnProperty(i.toString() + (j).toString())){
                            gears[i.toString() + (j).toString()] = new Array(number);
                        } else {
                            gears[i.toString() + (j).toString()].push(number);
                        }
                    }

                    if(
                        topSlice.match(/[^.0123456789]/) != null ||
                        bottomSlice.match(/[^.0123456789]/) != null ||
                        !".0123456789".includes(left) ||
                        !".0123456789".includes(right)
                    ){
                        count += Number(number);
                    }
                    number = "";
                }
            }
        }
        console.log("part1: " + count);
        console.log("part2: " + Object.entries(gears).filter((item) => item[1].length == 2).map((item) => item[1][0] * item[1][1]).reduce((acc, value) => acc + value));
    });
}

day03();