#include <iostream>
#include<string>
#include <sstream>
using namespace std;

template<class E>
class StackArray {
private:
	int maxsize;
	int top;
	E *stack;

public:
	StackArray(int sz){
		maxsize = sz;
		top = -1;
		stack = new E[maxsize];
	}
	int size(){
       return(top + 1);
	}

	bool isEmpty(){
    	if(top <= -1){
			return true;

		}
		else{
			return false;
		}
	}

	void push(E& elt){
		if(top == maxsize - 1 ){
			cout<<"Stack Full Exeption"<<endl;
		}
		else{
			top = top + 1;
			stack[top] = elt;
		}
	}

	E pop(){
		if(size() == 0)
		{
			cout<<"Stack Empty Exception"<<endl;
			return NULL;
		}
		else{
			int p = stack[top];
			stack[top] = NULL;
			top = top - 1;
			return p;
		}
	}

	E Top(){
		if(top < 0){
			cout<<"Stack Empty Exception"<<endl;
			return NULL;
		}
		else{
			return stack[top];
		}

	}
	void printstack(){
		if (isEmpty()){
			cout<< "Empty";
		}
		else{
			for (int i=0;i<=top;i++){
				if (stack[i]!=NULL){
					cout<<stack[i]<<" ";
				}
			}
			cout << endl;
			return;
		}
	}
};

int getValue(string s, int pos) {
    istringstream iss(s);
    string temp;
    iss>>temp;
    iss>>temp;
    if(pos==1) {
        return stoi(temp);
    }
    else {
        iss>>temp;
        return stoi(temp);
    }
}
//Driver Code
int main(){
	string noOfInputs,max,str;
	getline(cin, max);
 	StackArray<int> stack1(stoi(max));
 	getline(cin, noOfInputs);
 	for(int i=0;i<stoi(noOfInputs);i++){
 	    getline(cin, str); 
 	    
 	    if (str.substr(0, 1) == "S"){
 	       cout<< stack1.size()<<endl;
 	    }
 	    else if (str.substr(0,1) == "I"){
 	        //cout<<slist1.isEmpty()<<endl;
 	        if(stack1.isEmpty()){
 	            cout<<"True"<<endl;
 	        }
 	        else{
 	            cout<<"False"<<endl;
 	        }
 	    }
 	    else if (str.substr(0, 1) == "P"){
 	        int value = getValue(str, 1);
 	        stack1.push(value);
 	        stack1.printstack();
 	    }
 	    else if (str.substr(0, 1) == "O"){
 	        cout << stack1.pop()<<endl;
 	        stack1.printstack();
 	    }
 	    else if (str.substr(0, 1) == "T"){
 	        cout << stack1.Top()<<endl;
 	        stack1.printstack();
 	    }
 	    
 	}
}