const reader = require("fs");
const part1 = () => {
    const data = reader.readFile("input.txt", (err, data) => {
        const lines = new String(data).split("\r\n");

        let firstNumber = -1;
        let lastNumber = -1;
        let count = 0;
        for(let i = 0; i < lines.length; i++){
            for(let j = 0; j < lines[i].length; j++){
                if("123456789".includes(lines[i][j]) && firstNumber === -1){
                    firstNumber = lines[i][j];
                } else if("123456789".includes(lines[i][j])){
                    lastNumber = lines[i][j];
                }
            }
            
            if(firstNumber != -1 && lastNumber == -1){
                count += Number(firstNumber + firstNumber);
            } else if(firstNumber != -1 && lastNumber != -1){
                count += Number(firstNumber + lastNumber);
            }

            firstNumber = -1;
            lastNumber = -1;
        }

        console.log(count)
    })
}

const part2 = () => {
    const data = reader.readFile("input.txt", (err, data) => {
        const lines = new String(data).split("\r\n");

        const digits = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        };
        let numbersFound = [];
        let count = 0;
        let firstNumber = -1;
        let lastNumber = -1;
        const regex = new RegExp("(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))", "g");
        for(let i = 0; i < lines.length; i++){
            numbersFound = [...lines[i].matchAll(regex)];

            if(numbersFound.length === 1){
                firstNumber = numbersFound[0][1];
                lastNumber = numbersFound[0][1];
            } else if(numbersFound.length > 1){
                firstNumber = numbersFound[0][1];
                lastNumber = numbersFound[numbersFound.length - 1][1];
            } else if(numbersFound.length === 0){
                throw new Error("No numbers found")
            }

            if(firstNumber.length > 1){
                firstNumber = digits[firstNumber];
            } else if(firstNumber.length == 1){
                firstNumber = Number(firstNumber);
            }

            if(lastNumber.length > 1){
                lastNumber = digits[lastNumber];
            } else if(lastNumber.length == 1){
                lastNumber = Number(lastNumber);
            }
            count += Number(firstNumber.toString().concat("", lastNumber.toString()));
        }

        console.log(count)
    })   
}

part1();
part2();