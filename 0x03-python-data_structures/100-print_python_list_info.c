#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
  PyListObject *list = (PyListObject *)p;

  // Get the size of the list
  int size = PyList_Size(list);

  // Get the number of elements that are actually allocated
  int allocated = list->allocated;

  // Print the size and allocated information
  printf("[*] Size of the Python List = %d\n", size);
  printf("[*] Allocated = %d\n", allocated);

  // Print the elements of the list
  for (int i = 0; i < size; i++) {
    PyObject *item = PyList_GetItem(list, i);
    char *type = (char *)Py_TYPE(item)->tp_name;

    // Check if the element is a string
    if (strcmp(type, "str") == 0) {
      printf("Element %d: \"%s\"\n", i, PyString_AsString(item));
    } else {
      printf("Element %d: %s\n", i, type);
    }
  }
}
