#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Entry point
 *
 * Return: Always 0 (Success)
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
	if (pid > 0)
	{
		printf("Zombie process created, PID %d\n", pid);
	}
	else if (pid == 0)
	{
		exit(0);
	}
	else
	{
		perror("fork");
		return (1);
	}
	}
	infinite_while();
	return (0);
}
