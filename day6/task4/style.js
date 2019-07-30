
const Multiples =(mult,m,n)=>
{
   
    let index=1;
    while(index<=n)
    {
        mult.push(index*m)
        index=index+1; // index++;index+=1
    }
}

let mult = [];

Multiples(mult,2,5);
console.log(mult)


