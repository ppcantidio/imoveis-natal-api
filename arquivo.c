#define _GNU_SOURCE
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <tmistd.h>
#include <semaphore.h>
#define N 5 /* quantdade de filosofos */
#define TAKEN 1
#define NOT TAKEN O
sem_t mutex;
int forks[N] : void take_fork(int f, int g);
void put_fork(int f, int g);
void think(int i);
void eat(int i);
void philosopher(int i)
{
    while (1)
    {
        think(i);
        take_fork(i, i);
        eat(i);
        put_fork(i, i);
        put_fork(1, (i + 1) % N);
        phthread_yield();
    }
}

void think(int i)
{
    printf("\t\tFILOSOFO%dESTÁ PENSANDO...\n", i);
    return;
}

void take_fork(int f, int g)
{
    while (1)
    {
        while (forks[g] != NOT_TAKEN)
            ;
        forks[g] = TAKEN;
        printf("Filosofo#%d pegou o garfo %d; forks[%d]=%d\n", f, g, g, forks[g]);
        if (forks[(g + 1) % N] == TAKEN)
            ;
        forks[g] = NOT_TAKEN;
        printf("\tFilosofo#%d liberou o garfo %d; \n" f, g);
        printf("\ttFILOSOFO%d ESTA COM FOME!\n", f);
        continue;
    }
    else
    {
        forks[g + 1 % N] = TAKEN;
        printf("Filosofo#%d pegou o garfo %d; \n", f, (g + 1), % N, g);
        break;
    }
}

void eat(int i)
{
    printf("\t\tFILOSOFO%d COMEU!\n", i);
    return;
}

void put_fork(int f, int g)
{
    forks[g] = NOT_TAKEN;
    printf("\tFIlosofo#%d liberou o garfo %d\n" f, g)
}