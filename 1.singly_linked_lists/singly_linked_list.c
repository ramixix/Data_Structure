#include <stdio.h>
#include <stdlib.h>


typedef struct Node{
    int value;
    struct Node *next;
}Node;



Node *head = NULL;

int is_list_empty(){
    if(head == NULL)
        return 1;
    
    else
        return 0;
}


void add_node_to_front(int value){
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->value = value;
    new_node->next = head;
    head = new_node;

}


void remove_node_from_front(){
    if(is_list_empty()){
        printf("List Is Empty!!!\n");
        return;
    }
    Node *temp = head;
    head = head->next;
    free(temp);
}


void add_node_to_back(int value){
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->value = value;
    new_node->next = NULL;

    if(is_list_empty()){
        head = new_node;
    }
    else{
        Node *temp = head;
        while(temp->next != NULL){
            temp = temp->next;
        }

        temp->next = new_node;
    }
}

void remove_node_from_back(){
    if(is_list_empty()){
        printf("List Is Empty!!!\n");
    }

    else if( head->next == NULL){
        free(head);
        head = NULL;
    }

    else{
        Node *temp = head;
        Node *temp2= head->next;
        while(temp2->next != NULL){
            temp = temp->next;
            temp2 = temp2->next;
            
        }
        free(temp2);
        temp->next = NULL;
    }
    
}


void add_item_by_order(int value){
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->value = value;
    new_node->next = NULL;
    if(is_list_empty()){
        head = new_node;
    }
    else{
        Node *temp = head;
        if(temp->value > value){
            new_node->next = head;
            head = new_node;
            return;
        }

        while(temp->next != NULL && (temp->next)->value < value){
            temp = temp->next;
        }
        new_node->next = temp->next;
        temp->next = new_node;

    }
}


void remove_specific_node(int value){
    if(is_list_empty()){
        printf("List Is Empty!!!\n");
        return;
    }
    else{
        Node *temp = head;
        Node *temp2 = head->next;

        if(head->value == value){
            head = temp2;
            free(temp);
            return;
        }   
        while(temp2 != NULL){
            if(temp2->value == value){
                temp->next = temp2->next;
                free(temp2);
                return;
            }
            temp = temp->next;
            temp2 = temp2->next;
        }
        if(temp2 == NULL){
            printf("There Is No Such a Node With The Given Value.\n");
        }
    }

}


int find_length() {
   int length = 0;
   Node *current;
    for(current = head; current != NULL; current = current->next) {
      length++;
    }
   return length;
}

void print_list(){
    if(is_list_empty()){
       printf("List Is Empty!!!\n");
        return;
    }

    Node *temp = head;
    while(temp->next != NULL){
        printf("%d -> ", temp->value);
        temp = temp->next;
    }
    printf("%d\n", temp->value);
    
}

int main(int argc, char *argv[]){
    
    add_item_by_order(5);
    add_item_by_order(3);
    add_item_by_order(7);
    add_item_by_order(8);
    add_item_by_order(54);
    print_list();
    // remove_node_from_front();
    add_item_by_order(0);
    int b = find_length();
    print_list();
    // remove_node_from_back();
    // remove_node_from_back();
    // remove_node_from_back();
    // print_list();
    remove_specific_node(0);

    print_list();

    int a = find_length();
    printf("%d, %d ", a, b);
   
}