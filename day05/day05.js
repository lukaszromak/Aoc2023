const reader = require("fs");


const d5_part01 = () => {
    reader.readFile("input.txt", (err, data) => {
        const input = new String(data).split("\r\n\r\n");
        let seeds = input[0].split(": ")[1].split(" ").map(x => Number(x));
        let maps = input.slice(1)
            .map(x => x.split(":\r\n")[1].split("\r\n"))
            .map(x => x.map(x => x.split(" ").map(x => Number(x))));

        console.log(maps);
        for(let i = 0; i < seeds.length; i++){
            for(let j = 0; j < maps.length; j++){
                for(let k = 0; k < maps[j].length; k++){
                    if(seeds[i] >= maps[j][k][1] && seeds[i] < maps[j][k][1] + maps[j][k][2]){
                        seeds[i] = maps[j][k][0] + seeds[i] - maps[j][k][1];
                        k = maps[j].length;
                    }
                }
            }
        }
        console.log(Math.min(...seeds));
    });
}

const d5_part02 = () => {
    reader.readFile("input.txt", (err, data) => {
        const input = new String(data).split("\r\n\r\n");
        let seeds = input[0].split(": ")[1].split(" ").map(x => Number(x));
        let maps = input.slice(1)
            .map(x => x.split(":\r\n")[1].split("\r\n"))
            .map(x => x.map(x => x.split(" ").map(x => Number(x))));

        let min = 99999999;
        console.log(seeds.length);
        for(let i = 0; i < seeds.length; i += 2){
            console.log(i);
            for(let l = seeds[i]; l < seeds[i] + seeds[i + 1]; l++){
                let seed = l;
                for(let j = 0; j < maps.length; j++){
                    for(let k = 0; k < maps[j].length; k++){
                        if(seed >= maps[j][k][1] && seed < maps[j][k][1] + maps[j][k][2]){
                            seed = maps[j][k][0] + seed - maps[j][k][1];
                            k = maps[j].length;
                        }
                    }
                }
                if(seed < min){
                    min = seed;
                }
            }
        }
        console.log(min);
    });
}

d5_part01();
d5_part02();