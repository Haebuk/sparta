var age = 20;
// console.log(age);

var name = 'Jonde Doe';
// console.log(name);

var personArray = [10, 20, 30];
// console.log(personArray[0]);

var personDict = {"name": "John Doe", "age": 21};
// console.log(personDict['age']);

// if (personDict['age'] > 19) {
//     console.log('Here is your beer!')
// } else {
//     console.log('Get Out!')
// }

function isValidAge(person) {
    if (person['age'] > 19) {
        return true
    } else {
        return false
    }
}

var personArray = [
    {"name": "John Doe", "age": 20},
    {'name': 'Jane Doe', 'age': 19},
];

for (var i = 0; i < personArray.length; i++) {
    // console.log(personArray[i]['age'])
    if (isValidAge(personArray[i])) {
        // console.log('Here is your beer');
    } else {
        // console.log('Get Out')
    }
}

function getAgeAverage(personArray) {
	var average = 0;

	// 연령 평균을 구해주는 함수를 만들어 봅시다.
	// 평균은 총합을 갯수로 나눠주면 됩니다.
    var sum = 0;
    for (var i = 0; i < personArray.length; i++) {
        sum += personArray[i]['age'];
    }
    average = sum / personArray.length;

	return average;
}

var personArray = [
										{"name": "John Doe", "age": 20},
										{"name": "Jane Doe", "age": 19},
										{"name": "Fred Doe", "age": 32},
										{"name": "Chris Doe", "age": 45},
										{"name": "Layla Doe", "age": 37},
									];

// console.log(getAgeAverage(personArray)); // 30.6

const students = ['John', 'Jane', 'Alex'];

for (let i = 0; i < students.length; i++) {
    // console.log(students[i]);
}

// for of로 배열의 원소를 가져올 수 있음
for (let student of students) {
    // console.log(student)
}

// for in: 배열 인덱스 반환
for (let index in students) {
    // console.log(index)
}

// forEach: 배열 내부에 있는 값을 실행
students.forEach((student) => {
    // console.log(student)
})


// 함수의 기본 구조
function hello() {
	console.log("Hello function");
}

// 첫번째 arrow function
// 함수 이름 = (함수인자) => (arrow function) {실행될 코드 블럭}
const arrowFunction = () => {
	console.log("Hello arrow function");
}

// 두번째 arrow function
// {}가 없는 형태, 한 줄만 가능
const arrowFunctionWithoutReturn = () => console.log("Hello arrow function without return");

hello(); // Hello function
arrowFunction(); // Hello arrow function
arrowFunctionWithoutReturn(); // Hello arrow function without return