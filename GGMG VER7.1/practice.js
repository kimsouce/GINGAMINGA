var fs = require('fs');

var csv = require('fast-csv');

//animal.csv

var ws = fs.createWriteStream('animal.csv');

csv.
    write([
        {'Q': '북극곰은 겨울잠을 잔다', 'A': 'X', 'E': '동물이 겨울에 잠을 자는 이유는 먹이가 없기 때문. 북극곰은 겨울잠을 자지 않는다'},
        {'Q': '하마는 말의 일종이다', 'A': 'X', 'E': '하마는 돼지의 일종이다'},
        {'Q': '물고기는 기침을 한다', 'A': 'O', 'E': '물고기는 물이 오염될 수록 기침을 한다'},
        {'Q': '두꺼비는 이가 없다', 'A': 'O', 'E': '두꺼비는 이가 아예 없다'},
        {'Q': '철새는 이동 중에 잠을 잔다', 'A': 'O', 'E': '뇌의 절반씩 교대로 잠을 자는 가수면 상태에서 비행한다'}
    ], {headers : true})
    .pipe(ws);

    //plant.csv
    var ws = fs.createWriteStream('plant.csv');

    csv.
        write([
            {'Q': '버섯은 식물이다', 'A': 'X', 'E': '버섯은 균류에 속한다'},
            {'Q': '어성초는 비린 향이 난다', 'A': 'O', 'E': '어성초에서는 비린 향이 난다'},
            {'Q': '인삼은 꿀에 재 놓아야 좋다', 'A': 'X', 'E': '꿀에 재 놓으면 일종의 독소성분이 발생하므로 좋지 않다'},
            {'Q': '이끼는 건조하거나 햇빛이 잘 비치는 곳에서 잘 자란다', 'A': 'X', 'E': '이끼는 그늘지고 습기가 많은 곳에서 잘 자란다'},
            {'Q': '동충하초는 식물이다', 'A': 'X', 'E': '곤충류나 거미류에 기생하며 숙주가 죽은 후에 그 체표에 다양한 형상, 크기, 색상을 가진 자실체를 형성하는 곤충기생성 자낭균류이다'}
        ], {headers : true})
        .pipe(ws);

    //health.csv
    var ws = fs.createWriteStream('health.csv');

    csv.
        write([
            {'Q': '예방 접종은 병을 치료하기 위해서 하는 것이다', 'A': 'X', 'E': '예방접종은 병에 걸리지 않기 위하여 하는 것입니다'},
            {'Q': '사람들이 병에 걸리는 것은 반드시 균 때문이다', 'A': 'X', 'E': '병의 원인은 균뿐만이 아닙니다'},
            {'Q': '감기 균은 공기를 통해서 전염된다', 'A': 'X', 'E': '감기 균은 공기 중에 퍼져 다니다가 호흡기를 통해 감염됩니다'},
            {'Q': '음식을 아무리 잘 씻어도 병균을 완전히 씻어내는지는 못한다', 'A': 'O', 'E': '세제나 물로 아무리 깨끗하게 씻어도 균을 완전히 씻어내지는 못합니다'},
            {'Q': '음식물로 들어온 균은 대부분 위 속에서 죽는다', 'A': 'O', 'E': '위 속에는 아주 강한 산이 있어서 병균이 들어오면 견디지 못하고 죽습니다'}
        ], {headers : true})
        .pipe(ws);



    