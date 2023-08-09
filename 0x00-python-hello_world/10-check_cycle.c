#include "list.h"

/**
 * check_cycle - Check if the linked list contains a cycle
 * @list: Linked list for verification
 *
 * Returns: 1 if the list has a loop, 0 if not
 */
int check_cycle(listint_t *list)
{
        listint_t *slow = list;
        listint_t *fast = list;

        if (!list)
                return(0);

        while (slow && fast && fast -> next)
        {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast)
                        return(1);
        }

        return(0);
0x01-python-if_else_loops_functions}
