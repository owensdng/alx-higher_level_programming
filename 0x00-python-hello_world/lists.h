#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for educational purposes
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - Print all elements of a listint_t list
 * @h: Pointer to the head node of the list
 * Return: Number of nodes in the list
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint - Add a new node at the beginning of a listint_t list
 * @head: Pointer to the pointer of the head node
 * @n: Integer value to add to the new node
 * Return: Pointer to the new head node
 */
listint_t *add_nodeint(listint_t **head, const int n);

/**
 * free_listint - Free all nodes of a listint_t list
 * @head: Pointer to the head node of the list
 */
void free_listint(listint_t *head);

/**
 * check_cycle - Check if a loop exists in a linked list
 * @list: Pointer to the head of the list
 * Return: 1 if a cycle is found, 0 otherwise
 */
int check_cycle(listint_t *list);

#endif /* LISTS_H */
