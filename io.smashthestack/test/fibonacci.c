//http://projecteuler.net/index.php?section=problems&id=2
//
//Find all even numbers in a fibonacci sequence < 4000000
//

int main()
{
    unsigned long t1=0, t2=0, sum=0, total=0;
    int loop=0;

    //loop to 4000000 and start with 1
    t1 = 0;
    t2 = 1;
    for(loop=1; sum <= 4000000; loop++){
        sum = t1 + t2;
        if( !(sum%2) ){
            total += sum;
            printf("%lu ", sum);
        }
        t1 = t2;
        t2 = sum;
    }
    printf("sum:%lu\n", total);


}
