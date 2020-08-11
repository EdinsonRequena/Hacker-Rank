function factorial(n)
{
    if (n < 2)
        {
            return 1;
        }
    
    return n * factorial(n-1);
}


function main() {
    const n = +(readLine());
    
    console.log(factorial(n));
}