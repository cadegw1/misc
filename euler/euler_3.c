#include <stdio.h>
#include <stdbool.h>

// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

// Function that checks whether or not the inputted number is a prime number
bool b_prime_checker(int num)
{
    bool b_ret_val = true;
    for(int i = 2; i <= num/2; ++i)
    {
        if(num % i == 0)
        {
            b_ret_val = false;
            break;
        }
    }

    return b_ret_val; 
}

int main()
{
    const long long number = 10;
    int index = 1;
    while(index * index < number)
    {
        if(number % index == 0)
        {
            if(b_prime_checker(index) == true)
            {
                printf("\r\n%d", index);
            }
        }
        index++;
    }
    printf("\r\n%d\n", index-1);

    return 0;
}