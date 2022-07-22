const clock = document.querySelector('.clock');
const dateEl = document.querySelector('.date');

const todoBoxs = document.querySelectorAll('.todo-box');
const completes = document.querySelectorAll('.complete');
const checks = document.querySelectorAll('.material-icons.check');

// console.log(todoBoxs);
// console.log(writeDates);
// console.log(checks);

function getClock() {
    const date = new Date();
    const hours=String(date.getHours()).padStart(2, "0");
    const minutes=String(date.getMinutes()).padStart(2, "0");
    const seconds=String(date.getSeconds()).padStart(2, "0");
    
    clock.innerText = `${hours}시 ${minutes}분 ${seconds}초`; //텍스트 변경
}

getClock();
setInterval(getClock, 1000); //1초마다 반복

const days = [
  "일", "월", '화', '수', '목', '금', '토'
]

function getDate() {
  const date = new Date();
  const year = date.getFullYear();
  const mon = date.getMonth() + 1;
  const _date = date.getDate();
  const day = date.getDay();

  dateEl.innerText = `${year}년 ${mon}월 ${_date}일 ${days[day]}요일`;
}

getDate();

// function setCheck(e){
//   const idx = e.target.id;
//   completes[idx].classList.toggle('hidden')
// }

// checks.forEach((check, idx) => {
//   check.id = idx;
//   check.addEventListener('click', setCheck);
// })