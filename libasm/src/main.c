#include "libasm.h"

int main()
{
    // char* NULLtest = NULL;
    // char *invalid_buffer = (char *)0x12345678;  // Adresse invalide

    //printf("invalid = %s\n", invalid_buffer); // Segfault
    // int * tab = malloc(10 * sizeof(int));
    // for (int i = 0; i < 10; i++)
    // {
    //     tab[i] = i;
    // }

    // test for ft_strlen
    // BASE TEST
    // printf("test for strlen\n");
    // char* strlentest = "hello42";
    // printf("STR = %s\n", strlentest);
    // printf("strlen = %lu\n", strlen(strlentest));
    // printf("ft_strlen = %lu\n",ft_strlen(strlentest));
    // SEGFAULT
    // printf("test for segfault = %s\n", NULLtest);
    // printf("strlen = %lu\n", strlen(NULLtest));
    // printf("ft_strlen = %lu\n",ft_strlen(NULLtest));
    // WRONG TYPE
    // printf("wrong type\n");
    // printf("strlen = %lu\n", strlen(tab));
    // printf("ft_strlen = %lu\n",ft_strlen(tab));
    // printf("end of strlen test\n");

    // test for ft_strcpy
    // BASE TEST
    // printf("test for strcpy\n");
    // char* strcpytest = "hello42";
    // char* dest = malloc(strlen(strcpytest)+1);
    // char* ft_dest = malloc(strlen(strcpytest)+1);
    // printf("SRC = %s\n", strcpytest);
    // printf("strcpy = %s\n", strcpy(dest, strcpytest));
    // printf("strcpy dest = %s\n", dest);
    // printf("ft_strcpy = %s\n", ft_strcpy(ft_dest, strcpytest));
    // printf("ft_strcpy dest = %s\n", ft_dest);
    // SEGFAULT
    // printf("test for segfault = %s\n", NULLtest);
    // printf("strcpy = %s\n", strcpy(dest, NULLtest));
    // printf("ft_strcpy = %s\n", ft_strcpy(ft_dest, NULLtest));
    // WRONG TYPE
    // printf("wrong type\n");
    // printf("strcpy = %s\n", strcpy(tab, strcpytest));
    // printf("ft_strcpy = %s\n", ft_strcpy(tab, strcpytest));
    // printf("end of strcpy test\n");

    // test for ft_strcmp
    // BASE TEST
    // printf("test for strcmp\n");
    // char *strcmptest = "hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42hello42";
    // char *strcmptest2 = "hello42";
    // printf("S1 = %s\n", strcmptest);
    // printf("S2 = %s\n", strcmptest2);
    // printf("strcmp = %d\n", strcmp(strcmptest, strcmptest2));
    // printf("ft_strcmp = %d\n", ft_strcmp(strcmptest, strcmptest2));
    // printf("end of strcmp test\n");
    // SEGFAULT
    // printf("test for segfault = %s\n", NULLtest);
    // printf("strcmp = %d\n", strcmp(NULLtest, strcmptest2));
    // printf("ft_strcmp = %d\n", ft_strcmp(NULLtest, strcmptest2));
    // WRONG TYPE
    // printf("wrong type\n");
    // printf("strcmp = %d\n", strcmp(tab, strcmptest2));
    // printf("ft_strcmp = %d\n", ft_strcmp(tab, strcmptest2));
    // printf("end of strcmp test\n");

    // test for ft_write
    // BASE TEST
    // char *writetest = "hello42";
    // int fd = open("test.txt", O_CREAT | O_RDWR | O_APPEND, 0777);
    // if (fd == -1)
    // {
    //     perror("Error opening file");
    // }
    // int b_write = write(fd,writetest, 10);
    // printf(" write output = %d]\n", b_write);
    // printf("errno = %d\n", errno);
    // printf("ft_write\n[");
    // int ft_b_write = ft_write(fd, writetest, 10);
    // printf(" ft_write output = %d]\n", ft_b_write);
    // printf("errno = %d\n", errno);
    // close(fd);

    // test for ft_read
    //BASE TEST
    // printf("test for read\n");
    // int fd2 = open("test_read.txt",0);
    // if (fd2 == -1)
    // {
    //     perror("Error opening file");
    // }
    // char *readtest = malloc(10);
    // int b_read = read(fd2, invalid_buffer, 10);
    // printf("read output = %d\n", b_read);
    // printf("read = %s\n", readtest);
    // printf("errno = %d\n", errno);
    // char *ft_readtest = malloc(10);
    // int ft_b_read = ft_read(fd2, ft_readtest, 10);
    // printf("ft_read output = %d\n", ft_b_read);
    // printf("ft_read = %s\n", ft_readtest);
    // printf("errno = %d\n", errno);
    // close(fd2);

   // end test for ft_read

    // test for ft_strdup
    // BASE TEST
     printf("test for strdup\n");
    char *strdup_test = "hello42";
    printf("strdup (ADR = %p  STR = %s)\n",strdup_test, strdup_test);
    char *strdup_res = strdup(strdup_test);
    printf("strdup_res (ADR = %p  STR = %s)\n",strdup_res, strdup_res);
    char *ft_strdup_res = ft_strdup(strdup_test);
   printf("ft_strdup_res (ADR = %p  STR = %s)\n",ft_strdup_res, ft_strdup_res);
    free(strdup_res);
    free(ft_strdup_res);
    printf("end of strdup test\n");

    return 0;
}
