
// flatten an array

let arr = [
    [1,2],
    [3,4],
    [5,6,[7,[1,2,3]],9],
    [10,11]
]

let flattenedArray = [].concat(...arr);
console.log(flattenedArray)

console.log(arr.flat(3))

function customFlat(arr, dept=1) {
    let result = []
    arr.forEach(el => {
        if(Array.isArray(el) && dept > 0)
            result.push(...customFlat(el, dept-1))
        else result.push(el)
    });
    return result
}

console.log(customFlat(arr, 3))

// Implemented Promise.all()

function myPromiseAll(promises) {
    let result = []
    return new Promise((resolve, reject) => {
        promises.forEach((p, index) => {
            p.then((res) => { 
                result.push(res)
            })
            if (index === promises.length - 1) {
                resolve.result
            }
        }).catch((err)=> reject(err))
    })
}

const input = document.querySelector("input")
const defaultText = document.getElementById("default")
const debounceText = document.getElementById("debounce")
const throttleText = document.getElementById('throttle')

const updateDebounceText = debounce((text) => {
    debounceText.textContent = text
})

const updateThrolleText = throtlle((text) => {
    throttleText.textContent = text
})

input.addEventListener("input", e => {
    defaultText.textContent = e.target.value
    updateDebounceText(e.target.value) 
    updateThrolleText(e.target.value)
})

function debounce(cb, delay=1000) {
    let timeout
    return(...args) => {
        clearTimeout(timeout)
        timeout = setTimeout(()=> {
            cb(...args)
        }, delay)   
    }  
}

function throtlle(cb, delay = 1000) {
    let shouldWait = false
    let waitingArgs
    const timeoutFUnc = () => {
        if (waitingArgs == null) {
            shouldWait = false
        } else {
            cb(...waitingArgs)
            waitingArgs = null
            setTimeout(timeoutFUnc, delay)
        }
    }
    return (...args) => {
        if (shouldWait) { 
            waitingArgs = args
            return
        } 
        cb(...args)
        shouldWait = true

        setTimeout(timeoutFUnc, delay)
    }
}