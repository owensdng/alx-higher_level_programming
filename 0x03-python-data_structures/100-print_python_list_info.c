#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    int size, i;
    PyObject *obj;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid argument: Not a list\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Size of the Python List = %d\n", size);

    if (PyList_CheckExact(p))
    {
        printf("[*] Allocated = %d\n", size);
    }
    else
    {
        printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);
    }

    for (i = 0; i < size; i++)
    {
        printf("Element %d: ", i);

        obj = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(obj)->tp_name);
    }
}
