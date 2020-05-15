// exercises taken from https://eloquentjavascript.net/02_program_structure.html

function exercise2_1(){
    for (let line = "#"; line.length < 8; line += "#")
      console.log(line);
}


function exercise2_2(){
    for (let i = 1; i <= 100; i++){
        let output = "";
        if( i % 3 == 0) output += "Fizz";
        if( i % 5 == 0) output += "Buzz";
        console.log(output || i);
      }
}


function exercise2_3(){
    let size = 8, board = "";

    for (let i = 1; i <= size; i++ ){
        for (let k = 1; k <= size; k ++){
            board += (i + k) % 2 == 0 ? " " : "#"; 
        }
    board += "\n";
    }

    console.log(board);
}