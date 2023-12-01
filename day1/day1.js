const reader = require("fs");
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
        console.log(Number(firstNumber + lastNumber));
        if(firstNumber == -1 || lastNumber == -1){
            count += Number(firstNumber + lastNumber);
        }
        firstNumber = -1;
        lastNumber = -1;
    }

    console.log(count)
})
