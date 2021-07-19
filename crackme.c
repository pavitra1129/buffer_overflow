#include <stdio.h>

void secret() {
        printf("You found the secret function!\n");
        printf("Congrats!\n");
        printf("The password is: Rev3ngineering1sc00l!\n");
        exit(0);
}

int main() {
        char pass[] = "Rev3ngineering1sc00l!";
        char input[30];
        int valid = 0;

        printf("Enter the password! ");
        gets(input);

        if (!memcmp(input, pass, 22)) {
                valid = 1;
        }

        printf("\nChecking password...\n\n");

        if (valid) {
                printf("Successfully logged in!\nGood job!\n");
                exit(0);
        } else {
                printf("Login failed!\n");
        }

        return 0;
}




