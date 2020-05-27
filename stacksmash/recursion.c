#include<stdio.h>
int fact(int n)
{
	if(n <= 1)
		return 1;
	else
		return n*fact(n - 1);
}
int main()
{
	int a;
	a = fact(5);
	return 0;
}
