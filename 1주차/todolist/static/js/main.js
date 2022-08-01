const clock = document.querySelector('.clock');
const dateEl = document.querySelector('.date');

//const todoBoxs = document.querySelectorAll('.todo-box');
//const completes = document.querySelectorAll('.complete');
//const checks = document.querySelectorAll('.material-icons.check');


function getClock() {
    const date = new Date();
    const hours=String(date.getHours()).padStart(2, "0");
    const minutes=String(date.getMinutes()).padStart(2, "0");
    const seconds=String(date.getSeconds()).padStart(2, "0");
    
    clock.innerText = `${hours}시 ${minutes}분 ${seconds}초 `; //텍스트 변경
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

const date = new Date()
let currYear = date.getFullYear();
let currMon = date.getMonth() + 1;
let currDate = date.getDate();
let currDay = date.getDay();

// 이전 달의 마지막 날짜와 요일
let startDay = new Date(currYear, currMon - 1, 0);
let prevDate = startDay.getDate();
let prevDay = startDay.getDay();

// 이번 달의 마지막 날짜와 요일
let endDay = new Date(currYear, currMon, 0);
let nextDate = endDay.getDate();
let nextDay = endDay.getDay();

const yearMonth = document.querySelector('.year-month');
const arrowLeft = document.querySelector('.arrow_left');
const arrowRight = document.querySelector('.arrow_right');
const dateDiv = document.querySelector('.date-div')
const dates = document.querySelectorAll('.calendar-date')
const actives = document.querySelectorAll('.active')

const active = []
const prev = []

function setPrevNext(){
  startDay = new Date(currYear, currMon - 1, 0);
  prevDate = startDay.getDate();
  prevDay = startDay.getDay();

  endDay = new Date(currYear, currMon, 0);
  nextDate = endDay.getDate();
  nextDay = endDay.getDay();
}

function setActive(_year, _mon){
  active.length = 0;

  actives.forEach(act => {
    const str = act.innerText;
    let [y, m, d] = str.split(' ');
    y = Number(y);
    m = Number(m);
    d = Number(d);
    //console.log(y, m, d)
    if(y === _year && m === _mon){
      active.push(d)
    }
  })
}
//setActive(2022, 8)

// 오늘의 년, 월 설정
function setYearMonth(){
  yearMonth.innerText = `${currYear}년 ${currMon}월`
  setPrevNext();
  setActive(currYear, currMon)

  for(let k=0; k<prev.length; k++){
    prev[k].classList.remove('isContain')
  }
  prev.length = 0

  let i = 0;

  // 이전 달
  for(let p = prevDate- prevDay; p <= prevDate; p++){
    dates[i].innerText = p

    if(!dates[i].classList.contains('grey')){
      dates[i].classList.add('grey')
    }
    i++
  }

  for(let c = 1; c <= nextDate; c++){
    dates[i].innerText = c

    if(active.includes(c)){
      dates[i].classList.add('isContain')
      prev.push(dates[i])
    }

    if(dates[i].classList.contains('grey')){
      dates[i].classList.remove('grey')
    }

    i++;
  }
  for(let n = 1; i < 42; n++){
    dates[i].innerText = n
   
    if(!dates[i].classList.contains('grey')){
      dates[i].classList.add('grey')
    }
    i++
  }
}

setYearMonth();

arrowLeft.addEventListener('click', () => {
  if(currMon === 1){
    currMon = 12;
    currYear = currYear - 1;
  } else {
    currMon -= 1;
  }
  setYearMonth();
})

arrowRight.addEventListener('click', () => {
  if(currMon === 12){
    currMon = 1;
    currYear = currYear + 1;
  } else {
    currMon += 1;
  }
  setYearMonth();
})

const day = [
  '일', '월', '화', '수', '목', '금', '토'
]


dates.forEach(_date => {
  _date.addEventListener('click', () => {
    const clickDay = _date.innerText;
    currDay = clickDay
    console.log(currYear, currMon, clickDay, 'click')
    location.href=`/calendar/get?year=${currYear}&month=${currMon}&date=${clickDay}`
  })
})