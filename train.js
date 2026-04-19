/* B-TASK (Nodejs):

  ⭐Savol: Shunday function tuzing, u 1ta string parametrga ega bolsin, 
    hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
    MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

// ⭐ Masalaning yechimi:
function countDigits(str) {
  const arr = [...str]
  const c = arr.filter(ele => ele >= '0' && ele <= '9') 
  return c.length
}

const result = countDigits('ad2a58jk49u54y79wet0sfgb9')
console.log(`RESULT: ${result}`)





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