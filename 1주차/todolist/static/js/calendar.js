
let y = 0
let m = 0
let d = 0

function setDate(){
  const [ ,path] = location.href.split('?')
  console.log(path)
  let [year, month, day] = path.split('&')
  y = year.split('=')[1]
  m = month.split('=')[1]
  d = day.split('=')[1]
}

const formSubmit = document.querySelector('#submit-btn')
const todoForm = document.querySelector('.todo-form')
formSubmit.addEventListener('click', () => {
  setDate()
  
  todoForm.method = 'POST'
  // {% url 'calendar_get' %}
  todoForm.action = `/calendar/get?year=${y}&month=${m}&date=${d}`
  todoForm.submit()
})


const cancels = document.querySelectorAll('.cancel')
cancels.forEach(cancel => {
  cancel.addEventListener('click', (e) => {
    setDate()
    const id = e.target.id
    console.log(id)
    location.href = `/calendar/delete/${id}?year=${y}&month=${m}&date=${d}`
  })
})

const comps = document.querySelectorAll('.check')
comps.forEach(compelete => {
  compelete.addEventListener('click', (e) => {
    setDate()
    const id = e.target.id
    console.log(id)
    location.href = `/calendar/complete/${id}?year=${y}&month=${m}&date=${d}`
  })
})

const edits = document.querySelectorAll('.edit')
edits.forEach(edit => {
  edit.addEventListener('click', (e) => {
    setDate()
    const id = e.target.id
    console.log(id)
    location.href = `/calendar/edit/${id}?year=${y}&month=${m}&date=${d}`
  })
})