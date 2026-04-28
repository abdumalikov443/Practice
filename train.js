/* F-TASK (NodeJS)

  ⭐Savol: Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, 
  agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
  MASALAN: getReverse("hello") return true return qiladi
*/ 

// ⭐ Masalaning yechimi:
function findDoublers(str){
  let arr = [...str]
  
  for (let a = 0; a < arr.length; a++) {
    for (let b = a + 1; b < arr.length; b++) {
      if (arr[a] === arr[b]) {
        return true
      }
    }
  }
  return false
}

const result = findDoublers("hello")
console.log(`Result --> ${result}`)
//



/* E-TASK (NodeJS)

  ⭐Savol: Shunday function tuzing, u bitta string argumentni qabul qilib 
  osha stringni teskari qilib return qilsin.
  MASALAN: getReverse("hello") return qilsin "olleh"
*/

/* ⭐ Masalaning yechimi:
function getReverse(str){
  output = ""
  for (char of str) {
    output = char + output
  }
  return output
}

const result = getReverse("mitask")
console.log(`Result --> ${result}`)
*/



/* D-TASK (NodeJS)

  ⭐Savol: Shunday function tuzingki unga integerlardan iborat array pass bolsin va 
  function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
  MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
*/

/* ⭐ Masalaning yechimi:
function getHighestIndex(array){
  let max = array[0]
  let max_index = 0
  for (let i = 1; i < array.length; i++) {
    if (array[i] > max) {
      max = array[i]
      max_index = i
    }
  }
  return max_index
}

const result = getHighestIndex([32, 5, 25, 52, 58, 19])
console.log(`Result --> ${result}`)
*/



/* C-TASK (NodeJS)

  ⭐Savol: Shunday function tuzing, u 2ta string parametr ega bolsin, 
  hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
  MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
*/

/* ⭐ Masalaning yechimi:
function checkContent(a, b) { 
  const arr1 = [...a].sort()
  const arr2 = [...b].sort() 
  console.log(arr1, arr2)
  return arr1.join('') === arr2.join('') 
}

const result = checkContent("cmldeteop", "completed")
console.log(`RESULT: ${result}`)  
*/




/* B-TASK (Nodejs):

  ⭐Savol: Shunday function tuzing, u 1ta string parametrga ega bolsin, 
    hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
    MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

/* ⭐ Masalaning yechimi:
function countDigits(str) {
  const arr = [...str]
  const c = arr.filter(ele => ele >= '0' && ele <= '9') 
  return c.length
}

const result = countDigits('ad2a58jk49u54y79wet0sfgb9')
console.log(`RESULT: ${result}`)
*/




/* A - TASK (Nodejs):

  ⭐Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni 
    ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
    MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

/* ⭐ Masalaning yechimi:
function countLetter(a, b) {
  let n = 0;
  for (const c of b) {
    if(c == a) {
      n++;
    };
  };
  return n;
};

const result = countLetter('l', 'pineapple');
console.log("Solution:", result);
*/