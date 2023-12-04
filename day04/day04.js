const reader = require("fs")

const part1 = () => {
    reader.readFile("input.txt", (err, data) => {
        const games = new String(data)
            .split("\r\n")
            .map((x) => x.split(": ")[1].replace(/ [ ]+/g, " ").split(" | "))

        let cardLeft = [];
        let cardRight = [];
        let winning;
        let count = 0;

        for(let i = 0; i < games.length; i++){
            cardLeft = games[i][0].split(" ");
            cardRight = games[i][1].split(" ");
            winning = [...cardLeft].filter(x => cardRight.includes(x));

            if(winning.length > 0){
                count += Math.pow(2, winning.length - 1);
            }
        }

        console.log("part1: " + count);
        console.timeEnd("part1");
    })
}

const part2 = () => {
    reader.readFile("input.txt", (err, data) => {
        const games = new String(data)
            .split("\r\n")
            .map((x) => x.split(": ")[1].replace(/ [ ]+/g, " ").split(" | "))


        let cardLeft = [];
        let cardRight = [];
        let winning;
        let cards = new Array(games.length).fill(0); 
        
        for(let i = 0; i < games.length; i++){
            cardLeft = games[i][0].split(" ");
            cardRight = games[i][1].split(" ");
            winning = [...cardLeft].filter(x => cardRight.includes(x));

            cards[i]++;
            
            for(let k = 0; k < cards[i]; k++){
                for(let j = i + 1; j <= i + winning.size; j++){
                    cards[j]++;
                }
            }
        }
        console.log("part2: " + cards.reduce((acc, value) => acc + value))
        console.timeEnd("part2");
    })
} 

console.time("part1");
part1();

console.time("part2");
part2();