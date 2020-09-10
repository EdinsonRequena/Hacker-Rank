/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    var v = 'aeiou'

    for(var i = 0; i < s.length; i ++){
        if (v.includes(s[i])){
            console.log(s[i])
        }
    }

    for(var j = 0; j < s.length; j ++){
        if(!v.includes(s[j])){
            console.log(s[j])
        }
    }
    
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}