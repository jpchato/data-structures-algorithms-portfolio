let fizzBuzz = (number) => {
    if (number % 15 === 0) {
        console.log('fizzbuzz')
        return 
    }
    else if (number %5 ===0) {
        console.log('fizz')
        return
    }
    else if (number %3 ===0) {
        console.log('buzz')
        return
    }
    else {
        console.log(number)
        return
    }

} 


fizzBuzz(1)
fizzBuzz(3)
fizzBuzz(5)
fizzBuzz(15)
fizzBuzz(2)
// // ES6
// const multiplyES6 = (x, y) => { return x * y };