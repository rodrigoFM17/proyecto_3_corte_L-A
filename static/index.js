
const addValue = (e) => {
    const display = document.querySelector("#display")

    display.value += e.target.value
}

const deleteLast = () => {
    const display = document.querySelector("#display")
    display.value = display.value.substring(0, display.value.length - 1)
}

const deleteAll = () => {
    const display = document.querySelector("#display")
    display.value = ""
}

const calculate = () => {
    alert("negro")
}