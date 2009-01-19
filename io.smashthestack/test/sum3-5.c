//http://projecteuler.net/index.php?section=problems&id=1
//Add all multiples of 3 and 5 between 0-1000
//



int main()
// check mod 3 or 5 and add to an array
{
    int loop, store[1000];
    int index=0;
    unsigned long sum;

    //loop to 1000
    for( loop=1; loop<=1000; loop++){
    // check mod 3 or 5 and add to an array
        if( !(loop%3) || !(loop%5) ){ 
            store[index] = loop;
            index++;
        }else{
            continue;
        }
    }
    
    //add up all integers in the array
    index=0;
    while(store[index]){
        sum += store[index];
        index++;
    }
    printf("sum: %d\n", sum);




}
