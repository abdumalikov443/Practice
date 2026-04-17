console.log("MITASK --> A")

/* A - TASK:
⭐ Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni 
    ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
    MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

// Masalaning yechimi:
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