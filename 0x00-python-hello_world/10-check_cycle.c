#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;  // Slow-moving pointer
	listint_t *fast = list;  // Fast-moving pointer

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;            // Move slow pointer by one step
		fast = fast->next->next;      // Move fast pointer by two steps
		if (slow == fast)             // If they meet, a cycle is detected
			return (1);
	}

	return (0);  // No cycle found
}
