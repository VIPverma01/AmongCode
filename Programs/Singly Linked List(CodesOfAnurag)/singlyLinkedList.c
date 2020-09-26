#include<stdlib.h>
#include<stdio.h>

struct node
{
    int data;
    struct node *link;
}*head=NULL, *ptr, *temp, *curr;

void insBeg()
{
    temp=(struct node*)malloc(sizeof(struct node));
    printf("Enter Data : ");
    scanf("%d",&temp->data);
    temp->link=head;
    head=temp;
}

void insEnd()
{
    temp=(struct node*)malloc(sizeof(struct node));
    printf("Enter Data : ");
    scanf("%d",&temp->data);
    temp->link=NULL;
    ptr=head;
    while(ptr->link!=NULL)
        ptr=ptr->link;
    ptr->link=temp;
}

int countNode()
{
    int count=0;
    ptr=head;
    while (ptr!=NULL)
    {
        ptr=ptr->link;
        count++;
    }
    return count;
}

void insPos()
{
    int pos, count = countNode();
    printf("Enter Position : ");
    scanf("%d",&pos);
    if (pos==1)     insBeg();
    else if (pos==count+1)      insEnd();
    else if (pos>1 & pos<count+1)
    {
        int i;
        temp=(struct node*)malloc(sizeof(struct node));
        printf("Enter Data : ");
        scanf("%d",&temp->data);
        ptr=head;
        for (i=1;i<pos-1;i++)
            ptr=ptr->link;
        temp->link=ptr->link;
        ptr->link=temp;
    }
    else
        printf("Invalid Position\n");
}

void display()
{
    ptr=head;
    if(ptr==NULL)   printf("Empty List\n");
    else
    {
        while (ptr!=NULL)
        {
            printf("%d\t",ptr->data);
            ptr=ptr->link;
        }
        printf("\n");
    }
}

void delBeg()
{
    if (head==NULL)   printf("Empty List\n");
    else
    {
        ptr=head;
        head=head->link;
        free(ptr);
    }
}

void delEnd()
{
    if (head==NULL)   printf("Empty List\n");
    else
    {
        ptr=head;
        while(ptr->link!=NULL)
        {
            temp=ptr;
            ptr=ptr->link;
        }
        temp->link=NULL;
        free(ptr);
    }
}

void delPos()
{
    int pos, count = countNode();
    printf("Enter Position : ");
    scanf("%d",&pos);
    if (pos==1)     delBeg();
    else if (pos>1 & pos<=count)
    {
        int i;
        ptr=head;
        for(i=1;i<pos;i++)
        {
            temp=ptr;
            ptr=ptr->link;
        }
        temp->link=ptr->link;
        free(ptr);
    }
    else
        printf("Invalid Position\n");
}

void reverse() 
{ 
    ptr = NULL; 
    curr = head; 
    struct Node* next; 
    while (curr != NULL) 
    { 
        next  = curr->link;   
        curr->link = ptr;    
        ptr = curr; 
        curr = next; 
    } 
    head = ptr; 
} 

void main()
{
    int res;
    while (1)
    {
        printf(" 1 - insBeg \n 2 - insEnd \n 3 - insPos \n 4 - display \n 5 - delBeg \n 6 - delEnd \n 7 - delPos \n 8 - Reverse\n 9 - Exit\nEnter Response : ");
        scanf("%d",&res);
        switch(res)
        {
            case 1: insBeg(); break;
            case 2: insEnd(); break;
            case 3: insPos(); break;
            case 4: display(); break;
            case 5: delBeg(); break;
            case 6: delEnd(); break;
            case 7: delPos(); break;
            case 8: reverse(); break;
            case 9: exit(0); break;
        }
    }
}