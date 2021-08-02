// 객체 내용 출력하기
var personArray = [
    {"name": "John Doe", "age": 20},
    {"name": "Jane Doe", "age": 19},
    {"name": "Mark Bae", "age": 30},
    {"name": "Chris Doe", "age": 22},
    {"name": "Fred Doe", "age": 8},
]

for (let person of personArray) {
    console.log('His/her name is %s. He/She is %d years old.', person["name"], person["age"]);
}

// 홀수/짝수 구분 함수 만들어보기
function isEven(n) {
    if (n % 2 == 0) {
        return true
    } else return false
}
function isodd(n) {
    if (n % 2 != 0) {
        return true
    } else return false
}

console.log(isEven(2));
console.log(isEven(3));
console.log(isodd(5));
console.log(isodd(8));

// John Doe만 마실 수 있는 맥주
function checkName(person) {
    // 사람의 이름이 "john Doe" 일때만 true를 리턴
    if (person['name'] == 'John Doe') {
        return true
    } else return false
}

for (var person of personArray) {
    if (checkName(person)) {
        console.log('Here is your beer!', person['name']);
    } else {
        console.log('Get Out!', person['name']);
    }
}

// 미성년자만 찾아보기
function getChildrens(personArray) {
    under20years = []
    // 20세 미만의 사람들만 배열로 반환
    for (let person of personArray) {
        if (person['age'] < 20) {
            under20years.push(person)
        }
    }
    return under20years
}

console.log(getChildrens(personArray));