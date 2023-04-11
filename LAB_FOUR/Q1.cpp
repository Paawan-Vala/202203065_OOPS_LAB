#include<iostream>
using namespace std;
class Node
{
	public :
		int data;
		Node *next;
	Node(int data)
	{
		this->data = data;
		this->next = NULL;
	}
	~Node(){
		int value = this->data;
		if(this->next != NULL)
		{
			delete next;
			this->next = NULL;
		}
		cout<<"Memory is free"<<endl;
	}
};
void InsertAtHead(Node* &head, int d)
{
	Node* temp = new Node(d);
	if(head == NULL)
	{
		head = new Node(d);
		return;
	}
	temp->next = head;
	head = temp;
}
void InsertAtTail(Node* &tail, int d)
{
	Node* temp = new Node(d);
	tail->next = temp;
	tail = tail->next;	
}
void InsertAtAnyPosition(Node* &tail, Node* & head,int position, int d){
	if(position ==1)
	{
		InsertAtHead(head,d);
		return;
	}
	Node* temp = head;
	int c=1;
	while(c<position-1){
		temp = temp->next;
		c++;
	}
	if(temp->next == NULL){
		InsertAtTail(tail,d);
		return;
	}
	Node*  nodetoinsert = new Node(d);
	nodetoinsert->next = temp->next;
	temp->next = nodetoinsert;
}
void print(Node* &head){
	Node* temp = head;
	while(temp != NULL){
		cout<<temp->data<< "->";
		temp = temp->next;
	}
	cout<<"NULL";	
	cout<<endl;
}
void deleteNode(int position, Node* &head){
	if(position == 1){
		Node* temp = head;
		head = head->next;
		temp->next = NULL;
		delete temp;
	}
	else{
		Node* curr = head;
		Node* prev = NULL;
		int c=1;
		while(c< position){
			prev = curr;
			curr = curr->next;
			c++;
		}
		prev->next = curr->next;
		curr->next = NULL; 
		delete curr; 
	}
}
int main(){
	int n;
	cout<<"Enter the value of head node : ";
	cin>>n;
	Node* node1 = new Node(n);
	Node* head = node1;
	Node* tail = node1;
	InsertAtHead(head,7);
	print(head);
	InsertAtHead(head,9);
	print(head);
	InsertAtTail(tail,14);
	print(head);
	InsertAtTail(tail,524);
	print(head);
	InsertAtAnyPosition(tail,head,4,7);
	print(head);
	cout<<"Head "<<head->data <<endl;
	cout<<"Tail "<<tail->data <<endl;
	deleteNode(9,head);
	print(head);
	deleteNode(7,head);
	print(head);
    cout<<"Tail "<<tail->data <<endl;
	cout<<"Head "<<head->data <<endl;
	return 0;
}