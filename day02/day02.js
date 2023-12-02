const reader = require("fs");

const findPowerOfGame = (gameSubsets) => {
    let colorMax = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    let amount;
    let color;
    for(let j = 0; j < gameSubsets.length; j++){
        cubes = gameSubsets[j].split(", ");
        for(let k = 0; k < cubes.length; k++){
            amount = Number(cubes[k].split(" ")[0]);
            color = cubes[k].split(" ")[1];
            if(amount > colorMax[color]){
                colorMax[color] = amount;
            }
        }
    }
    return colorMax["red"] * colorMax["green"] * colorMax["blue"];   
}

const isGamePossible = (gameSubsets) => {
    const maxCubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    let color = "";
    let cubes = [];
    let amount = -1;
    for(let j = 0; j < gameSubsets.length; j++){
        cubes = gameSubsets[j].split(", ");
        for(let k = 0; k < cubes.length; k++){
            amount = Number(cubes[k].split(" ")[0]);
            color = cubes[k].split(" ")[1];
            if(amount > maxCubes[color]){
                return false;
            }
        }
    }
    return true;
}

const part1 = () => {
    reader.readFile("input.txt", (err, data) => {
        const games = new String(data).split("\r\n").map((line) => line.split(":")[1].trim());

        let countPt1 = 0;
        let countPt2 = 0;
        for(let i = 0; i < games.length; i++){
            gameSubsets = games[i].split("; ")
            if(isGamePossible(gameSubsets)){
                countPt1 += i + 1;
            }
            countPt2 += findPowerOfGame(gameSubsets);
        }

        console.log(`part 1: ${countPt1}`);
        console.log(`part 2: ${countPt2}`)
    })
}

part1();