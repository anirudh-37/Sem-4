#include<string>
#include<iostream>
#include <vector>
#include <sstream>
#include<iterator>
using namespace std;

template<class E>
class QueueArray {
private:
	int maxsize;
	int front;
	int rear;
	E *queue;

public:
	QueueArray(int sz){
		maxsize = sz;
		front = -1;
		rear = -1;
		size = 0;
		queue = new E[maxsize];
	}
	int Size(){
		return(size);
	}

	bool isEmpty(){
		return(Size() == 0);
	}

	void enqueue(E& elt){
		if(Size() == maxsize){
			cout<<"Overflow"<<endl;
		}
		else{
			if(rear == -1){
				rear = 0;
				}
			queue[rear] = elt;
			rear = (rear+1)%maxsize;
			size++;
		}
	}

	E dequeue(){
		if(Size() == 0){
			cout<<"QueueEmptyException"<<endl;
		}
		else{
			  E temp;
			front = (front+1)%maxsize;
			temp = queue[front];
			size = (maxsize-front+rear)%maxsize;
			return temp;
	}
	}

	E front(){
		
	}
	void displayqueue(){
		if isEmpty(){
			cout<< "Empty";
		}
		else{
			for (int i=0;i<maxsize;i++){
				if queue[i]!=NULL{
					cout<<queue[i]<<" ";
				}
			}
			cout << endl;
			return;
		}
	}
};

void getInput(string const &inputStr,vector<string> &myOutput)
{
    stringstream ss(inputStr);
    string st ="";
    while (getline(ss, st, ' ')) {
        myOutput.push_back(st);
    }
}
char trim(string str) 
{ 
   return str[0];
} 
//Driver Code
int main(){
	string noOfInputs,max,str;
	getline(cin, max);
 	QueueArray<int> queue(stoi(max));
 	getline(cin, noOfInputs);
 	for(int i=0;i<stoi(noOfInputs);i++){
 	    vector<string> myOutput;
 		str="";
 	    getline(cin, str); 
 	    getInput(str,myOutput);
 	    auto it = myOutput.begin();
        //Note:if there is a sequence expected beyond first char, then DO NOT use trim()
 	    if(it[0] == "E"){
 	    	++it;
 	    	queue.enqueue(stoi(*it));
 	        queue.displayQueue();
 	    }
 	    else if(trim(it[0]) == 'D'){
 	    	queue.dequeue();
 	        queue.displayQueue();
 	    }
 	    else if(trim(it[0]) == 'S'){
 	    	cout<<queue.Size()<<endl;
 	    }
 	    else if(trim(it[0]) == 'F'){
 	    	cout<<queue.first()<<endl;
 	    }
 	    else if(trim(it[0]) == 'I'){
 	    	if(queue.isEmpty()){
 	    	    cout<<"True"<<endl;
 	    	}
 	    	else{
 	    	    cout<<"False"<<endl;
 	    	}
 	    }
 	    else{
 	        cout<<"Invalid Input"<<endl;
 	    }
 	}
}