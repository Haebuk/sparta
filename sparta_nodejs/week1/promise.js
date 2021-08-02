const isReady = false;
// 1. Producer
const promise = new Promise((resolve, reject) => {
  console.log("Promise is created!"); // pending
  if (isReady) {
    resolve("It's ready"); // resolved
  } else {
    reject("Not ready"); // rejected
  }
});

// 2. Consumer
promise
  .then(messsage => { // 정상 작동하면 then으로 빠짐 resolve에 담긴 값이 message로 빠짐
    console.log(messsage);
  })
  .catch(error => { // 문제 발생 시 catch로 넘어옴
    console.error(error);
  })
  .finally(() => { // 최종
    console.log("Done");
  });

// Promise is created!
// It's ready
// Done

async function f() {

    let promise = new Promise((resolve, reject) => {
      setTimeout(() => resolve("완료!"), 1000)
    });
  
    let result = await promise; // 프라미스가 이행될 때까지 기다림 (*)
  
    console.log(result); // "완료!"
  }
  
  f();