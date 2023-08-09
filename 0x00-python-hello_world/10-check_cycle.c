#include "lists.h"

/**
 * check_cycle - Detects a cycle in a linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if a cycle exists, 0 if not.
 */
int check_cycle(listint_t *head)
{
    listint_t *slow_ptr = head;
    listint_t *fast_ptr = head;

    // Check if the linked list is empty
    if (!head)
        return 0;

    // Use Floyd's cycle-finding algorithm
    while (slow_ptr && fast_ptr && fast_ptr->next)
    {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;

        // If the pointers meet, a cycle is found
        if (slow_ptr == fast_ptr)
            return 1;
    }

    // No cycle was found
    return 0;
}
